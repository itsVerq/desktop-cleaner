import os
import shutil


DOCUMENTS = ('.txt', '.doc', '.docm', '.docx', '.dot', '.odt', '.pdf',
             '.csv', '.ods', '.ots', '.stc', '.sxc', '.xla', '.xlk', '.xlr', '.xls', '.xlsm', '.xlsx',
             '.odp', '.otp', '.pps', '.ppt', '.sti', '.sxi')


def delete_empty_dir(path):
    with os.scandir(path) as it:
        for entry in it:
            if os.path.isdir(entry.path) and (not any(os.scandir(entry.path))):
                os.rmdir(entry.path)
                print('Deleted empty directory:', entry.path)


def create_dir(extensions_list, dir_name, path):
    new_dir_path = path + r'\{}'.format(dir_name)
    if os.path.exists(new_dir_path):
        return

    with os.scandir(path) as it:
        if any(entry.name.endswith(extensions_list) for entry in it):
            os.mkdir(new_dir_path)
            print('Created new directory: {}, path: {}'.format(dir_name, new_dir_path))


def move_file_to_dir(extensions_list, path, dest_path):
    if not os.path.exists(dest_path):
        return

    with os.scandir(path) as it:
        for entry in it:
            if entry.name.endswith(extensions_list) and os.path.isfile(entry.path):
                shutil.move(entry.path, dest_path)
                print('Moved {} to {}'.format(entry.name, dest_path))


if __name__ == '__main__':
    desktop_path = os.path.expanduser('~') + r'\Desktop'
    delete_empty_dir(desktop_path)
    create_dir(DOCUMENTS, 'Documents', desktop_path)
    move_file_to_dir(DOCUMENTS, desktop_path, desktop_path + r'\Documents')
