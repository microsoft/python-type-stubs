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

        # Skip docstrings
        l = line.strip()
        if l == '"""':
            in_doc = not in_doc
            i += 1
            continue
        if in_doc:
            i += 1
            continue

        if line.startswith(lookfor):
            if class_:
                i += 1
                lookfor = f'def {method}('
                while i < len(stublines):
                    line = stublines[i].strip()

                    if line == '"""':
                        in_doc = not in_doc
                        i += 1
                        continue
                    if in_doc:
                        i += 1
                        continue

                    if line.startswith('class '):
                        raise Exception(f'{stubfile}:{i} Method {method} not found in class {class_}')
                    if line.startswith(lookfor):
                        break
                    i += 1
                else:
                    raise Exception(f'{stubfile}:{i} Method {method} not found in class {class_}')
            # We have found the first line of the method. The signature can
            # span multiple lines, so we need to look for '...\n' to 
            # find the end
            j = i
            end = i
            while j < len(stublines):
                line = stublines[j].strip()
                if line.endswith(' ...'):
                    stublines[j] = line[:-4] + '\n'  # Discard the ...
                    end = j
                    break
                j += 1
            else:
                raise Exception(f'Could not find end of method {method}')
            j += 1
      
            # We now have the start and end of the method
            if class_:
                stublines[end] += f'        """\n{doc}\n        """\n        pass\n'
            else:
                stublines[end] += f'    """\n{doc}\n    """\n    pass\n'

            newstublines = stublines[:end+1]
            newstublines += stublines[j:]
            break

        i += 1
    else:
        raise Exception(f'{stubfile}: Could not find target {class_} {method}')

    with open(stubfile, 'w') as f:
        f.writelines(newstublines)
    print(f'Patched {class_} {method} in {stubfile}')

