import os


def is_exist(path):
    if not os.path.exists(path):
        return False
    else:
        return True
        

def is_done(path, palabraABuscar="aaaaaaa"):
    with open(path) as _f:
        contents = _f.read()
    if palabraABuscar in contents.lower():
        return True
    elif "no" in contents.lower():
        return False
    else:
        return False