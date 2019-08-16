import os
import glob
import shutil


def stu_activities(src_directory, dst_directory):
    def copy_file(src_directory=".", dst_directory="."):
        counter = 0
        for src_file in glob.glob(src_directory + os.sep + '*', recursive=True):
            dst_file = dst_directory + os.sep + os.path.basename(src_file)
            try:
                shutil.copyfile(src_file, dst_file)
                counter += 1
            except shutil.SameFileError:
                print("Source and Destination are same !!!")
                break
            except:
                print("Un known Error in copying!!!")
        return counter

    file_counter = 0
    for folder in glob.glob(src_directory + os.sep + '**/Stu_*', recursive=True):
        for file in glob.glob(folder + os.sep + '*'):
            file_counter += copy_file(file, dst_directory)

    print(f"{file_counter} file(s) copied.")


if __name__ == "__main__":
    stu_activities(r"/Users/vsiddaia/Downloads/", r"./CyberSecurity-Notes")
    #pptx_copy(r"/Users/vsiddaia/Downloads/", r"/Users/vsiddaia/Downloads/")
