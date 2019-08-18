import os
import errno


def folder_structure(base_directory="."):
    """
    function folder_structure would have the following functionality:
    * Creates a directory called `CyberSecurity-Notes` in the current working directory
    * Within the `CyberSecurity-Notes` directory, creates 24 sub-directories (sub-folders), called `Week 1`, `Week 2`, `Week 3`, and so on until up through `Week 24`
    * Within each week directory, create 3 sub-directories, called `Day 1`, `Day 2`, and `Day 3`
    :param base_directory: input parameter is not specified would create a folder structure in the same directory
    :type base_directory: path/raw string
    :return: None
    :rtype: None
    """
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