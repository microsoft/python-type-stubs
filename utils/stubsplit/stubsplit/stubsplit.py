import os


# TODO: 
# - rewrite these as FSMs; will probably be cleaner and more 
#   maintainable long-term. Right now split() uses a for-in
#   loop which requires buffering some past content. For merge
#   I used indexing instead which avoided that, but it does
#   mix metaphors; using FSMs for both could be more consistent
#   and possible reuse the same 'driver' for both.
# - handle nested classes. This isn't urgent as we likely won't 
#   have any docstrings in these, but we should at least not
#   break.


def split(stubroot, docroot, fname, verbose):
    """
    Given the path to a .pyi file in `fname` as a path relative to `stubroot`,
    split it into a docstring part and a stub part. The stub part should get 
    written to the original file, and the docstring part should be written to
    a file with a .ds extension at the same relative path but under `docroot`.

    So for example, if called with `split('orig', 'target', 'module/__init__.py')`,
    you will end up with a stripped version of the stub in `orig/module/__init__.py`,
    and the docstrings in `target/module/__init__.py.ds`.

    The docstring file will preserve `class` lines, and the signature of the 
    specific function/method.

    The inverse function is `combine`.
    """
    stubfile = os.path.join(stubroot, fname)
    docfile = os.path.join(docroot, fname) + '.ds'
    docpath, _ = os.path.split(docfile)
    if not os.path.exists(docpath):
        os.makedirs(docpath)
    if not os.path.exists(stubfile):
        raise Exception(f'Missing stub file {fname}')
    with open(stubfile) as f:
        stublines = f.readlines()
    newstublines = []    
    newdoclines = []
    defbuff = None
    classbuff = None
    indoc = False
    target = newstublines
    gotclose = False

    # TODO: handle split lines. This is more urgent as the stubs will likely be 
    #    reformatted.
    for line in stublines:
        ls = line.strip()
        if defbuff and defbuff.find(')') > 0:
            if ls[:3] == "'''" or ls[:3] == '"""':  # start of docstring
                if classbuff and defbuff[0] == ' ':
                    newdoclines.append('\n')
                    newdoclines.append(classbuff)
                newstublines.append(defbuff[:-1] + ' ...\n')
                newdoclines.append(defbuff)
                indoc = True
                classbuff = None
            else:
                newstublines.append(defbuff)
                if defbuff[0] == 'd':  # top level def?
                    classbuff = None
            defbuff = None

        if indoc:  # Keep adding to docstring until we hit a 'pass' line
            newdoclines.append(line)
            if gotclose and ls == 'pass': 
                indoc = False
            else:
                gotclose = ls.find( "'''") >= 0 or ls.find('"""') >= 0
        elif ls[:4] == 'def ':
            defbuff = line
        elif defbuff and defbuff.find(')') < 0: # Handle split lines; is this enough?
            defbuff += line
        else:
            # For now we handle top-level classes only
            if line[:6] == 'class ':
                classbuff = line
            newstublines.append(line)

    if defbuff:
        newstublines.append(defbuff)

    with open(stubfile, 'w') as f:
        f.writelines(newstublines)

    if len(newdoclines):
        with open(docfile, 'w') as f:
            f.writelines(newdoclines)


def combine(stubroot, docroot, fname, verbose):
    """
    Given the path to a .pyi file in `fname` as a path relative to `origroot`,
    and given that a similar file exists under `docroot` with the same relative
    path but an additional `.ds` suffix, combine these and replace the original
    stubfile with one that has the docstrings merged in.

    The inverse function is `split`.
    """   
    stubfile = os.path.join(stubroot, fname)
    docfile = os.path.join(docroot, fname) + '.ds'
    if not os.path.exists(stubfile):
        raise Exception(f'Missing stub file {fname}')
    if not os.path.exists(docfile):
        raise Exception(f'Missing doc file {fname}.ds')
    with open(stubfile) as f:
        stublines = f.readlines()
    with open(docfile) as f:
        doclines = f.readlines()
    if len(doclines) == 0:
        print(f'No docs found in {docfile}')
        return

    # Gather together all the top-level functions and all the classes
    # in dicts. That way we can be resilient to reorderings, if not
    # file moves yet.
    if verbose:
        print(f'Gathering docs from {docfile}')

    def gather_def(lines, i):
        ln = lines[i].strip()
        name = ln[4:ln.find('(')]
        start = i
        i += 1
        while i < len(lines):
            ln = lines[i].strip()
            i += 1
            if ln == 'pass':
                break
        return name, lines[start:i], i

    top_level = {}
    classes = {}
    i = 0
    while i < len(doclines):
        ln = doclines[i]
        if ln[:6] == 'class ':
            name = ln[6:min(ln.find('('), ln.find(':'))]
            i += 1
            methods = {}
            classes[name] = methods
            if verbose:
                print(f'{i+1}: class {name}')
            while i < len(doclines) and doclines[i][0] == ' ':
                name, deflines, i = gather_def(doclines, i)
                methods[name] = deflines
                if verbose:
                    print(f'{i+1}:     def {name}')
        elif ln[:4] == 'def ':
            name, deflines, i = gather_def(doclines, i)
            top_level[name] = deflines
            if verbose:
                print(f'{i+1}: def {name}')
        elif len(ln.strip()) > 0:
            raise Exception(f'Unhandled line {i}: "{ln}"')
        else:
            i += 1

    # Now output the new stub lines. If we find a top-level method
    # or class that is in our gathered data, substitute the original
    # line for the gathered version.

    print(f'Merging docs from {docfile} into {stubfile}')
    newstublines = []

    i = 0
    while i < len(stublines):
        ln = stublines[i]
        i += 1
        if ln[:6] == 'class ':
            name = ln[6:min(ln.find('('), ln.find(':'))]
            methods = classes[name] if name in classes else {}
            if methods.keys():
                print(f"Annotating class {name}")
            elif verbose:
                print(f'No methods found for class {name}')
            newstublines.append(ln)
            while i < len(stublines):
                # Either we have a indented line or a top-level
                # construct again
                ln = stublines[i]
                if ln[0].isalpha() or ln[0] == '@':
                    break
                i += 1
                ls = ln.strip()
                if ls[:4] == 'def ':
                    name = ls[4:ls.find('(')]
                    if name in methods:
                        # in case this is an overload, document same occurrence. To do that we need to 
                        # do a full signature comparison which may span several lines.
                        # Note that this is not robust in the face of running formatters with
                        # different line lengths. We should really reconstruct the signature line
                        # ourselves with normalized formatting. Ain't nobody got time for that.
                        # Given Python functions are not polymorphic and so the names should be
                        # unique (ignoring @overloads), a better approach would be to change 
                        # the split process so that it drops signatures and just stores function name
                        # or classname.methodname keys along with the docstrings, and then we can 
                        # just reinsert those ourselves on the first instance we find, instead of
                        # matching the exact instance.
                        lines = methods[name]
                        j = -1
                        while stublines[i + j].find(')') < 0: # Check all lines of signature for match
                            if stublines[i + j] != lines[j + 1]:
                                break
                            j += 1
                        # For last line of signature, stop matching at closing ')'
                        if stublines[i + j][:stublines[i + j].find(')')] == lines[j + 1][:lines[j + 1].find(')')]:
                            print(f"    Annotating method {name}")
                            newstublines.extend(lines)
                            del methods[name]  # Only doc first occurrence
                            # If split line skip rest of signature
                            i += j + 1
                        else:
                            newstublines.append(ln)
                    else:
                        newstublines.append(ln)
                else:
                    newstublines.append(ln)
        elif ln[:4] == 'def ':
            name = ln[4:ln.find('(')]
            if name in top_level:
                print(f"Annotating function {name}")
                newstublines.extend(top_level[name])
                while ln.find(')') < 0: # If wrapped we need to skip the rest of the signature
                    ln = stublines[i]
                    i += 1
                del top_level[name]
            else:
                newstublines.append(ln)
        else:
            newstublines.append(ln)

    with open(stubfile, 'w') as f:
        f.writelines(newstublines)
