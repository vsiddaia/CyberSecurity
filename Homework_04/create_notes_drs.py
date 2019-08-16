import os
import errno


def folder_structure(base_directory="."):
    def create_folder(directory):
        try:
            os.makedirs(directory)
            return True
        except OSError as error_id:
            if errno.EEXIST == error_id.errno:
                return True
            elif errno.EPERM == error_id.errno:
                print(f"Error in creating directory, {directory} permission denied !!! ")
            else:
                print(type(error_id))
                print(f"Error in creating directory, {directory} please verify !!! ")
        return False

    for week in range(1, 25):
        for day in range(1, 4):
            # print(dir_path)
            dir_path = base_directory + os.sep + 'CyberSecurity-Notes' + os.sep + 'Week_{:02d}'.format(week) + os.sep + \
                       'Day_{:d}'.format(day)
            create_folder(dir_path)

if __name__ == "__main__":
    folder_structure()