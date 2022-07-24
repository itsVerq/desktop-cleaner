import os


def delete_empty_dir(path):
    with os.scandir(path) as it:
        for entry in it:
            if os.path.isdir(entry.path) and (not any(os.scandir(entry.path))):
                os.rmdir(entry.path)
                print('Deleted empty folder:', entry.path)


if __name__ == '__main__':
    desktop_path = os.path.expanduser('~') + r'\Desktop'
    delete_empty_dir(desktop_path)


