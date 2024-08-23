# Problem discussion:
# Given a path. The canonical path should have the following format:
#  - Starts with '/'.
#  - Any two directories are seperated by a single '/'.
#  - Only contains directories from the root directory 'The current base directory', no '.' or '..'.
# Given a path return canonical path.
# Constraints:
#  1 <= path.length <= 3000.
#  Path is a valid UNIX path.
#  path contains letters, digits, dots and uderscores.

def get_caonical_path(path):
    path = path.replace('\\','/')
    canonical = []
    for p in path.split('/'):
        if p == '/':
            pass
        elif p == '.':
            pass
        elif p == '..':
            pass
        else:
            canonical.append(p)
    
    return '/' + '/'.join(canonical)
print(get_caonical_path(r'..\E:/Python Tuts\.\..\DataStructures'))