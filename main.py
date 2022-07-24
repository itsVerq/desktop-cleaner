import os

if __name__ == '__main__':
    dir_name = os.path.expanduser('~') + r'\Desktop'

    with os.scandir(dir_name) as it:
        for entry in it:
            if os.path.isdir(entry.path) and (not any(os.scandir(entry.path))):
                os.rmdir(entry.path)
                print('Deleted empty folder:', entry.path)
