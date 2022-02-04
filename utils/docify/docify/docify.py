import os
import sys


def docify(stubfile, class_, method, doc, verbose):
    if not os.path.exists(stubfile):
        raise Exception(f'Missing stub file {stubfile}')
    with open(stubfile) as f:
        stublines = f.readlines()

    lookfor = f'class {class_}' if class_ else f'def {method}('
    i = 0
    in_doc = False
    while i < len(stublines):
        line = stublines[i]

        # Look for docstring start/end, as we want to skip docstrings 
        # as they can mess with the parser. We use a simple check 
        # that relies on """ being on a line on its own, which is 
        # true of the docstrings we add at least.

        if line.strip() == '"""':
            in_doc = not in_doc

        elif not in_doc and line.startswith(lookfor):
            # If we are looking for a method, we have found the 
            # class but need to keep going...
            if class_:
                i += 1
                lookfor = f'def {method}('
                while i < len(stublines):
                    line = stublines[i].strip()
                    if line == '"""':
                        in_doc = not in_doc
                    elif not in_doc:
                        if line.startswith('class '):
                            raise Exception(f'{stubfile}:{i} Method {method} not found in class {class_}')
                        if line.startswith(lookfor):
                            break
                    i += 1
                else:  # We're all out of lines and didn't find the method
                    raise Exception(f'{stubfile}:{i} Method {method} not found in class {class_}')

            # We have found the first line of the method. The signature can
            # span multiple lines, so we need to look for '...\n' to find the end
            j = i
            end = i
            while j < len(stublines):
                line = stublines[j].rstrip()
                if line.endswith(' ...'):
                    end = j
                    break
                j += 1
            else:
                raise Exception(f'Could not find end of method {method}')
            break

        i += 1
    else:
        raise Exception(f'{stubfile}: Could not find target {class_} {method}')

    # We now have the start and end of the method. Discard the " ..."
    # and add the docstring and a 'pass'.
    if class_:
        stublines[end] = f'{line[:-4]}\n        """\n{doc}\n        """\n        pass\n'
    else:
        stublines[end] = f'{line[:-4]}\n    """\n{doc}\n    """\n    pass\n'

    with open(stubfile, 'w') as f:
        f.writelines(stublines)

    print(f'Patched {class_} {method} in {stubfile}')

