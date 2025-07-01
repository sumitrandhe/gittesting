import os

def check_file(path1):
    if os.path.exists(path1):
        return True
    else:
        return False

def remove_file(path1):
    return os.remove(path1)