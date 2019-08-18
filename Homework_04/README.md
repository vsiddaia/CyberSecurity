# Instructions

In this exercise, you will use Python to complete four practical challenges:
* Creating 24 directories for each week of class, each containing 3 folders for each day of class

* Copying files from `~/Downloads` into the current directory
* Adding the copy script to the PATH
* Add an alias for the copy script to `~/.bashrc`

---

## Class Notes Folder

Create a script called `create_notes_drs.py`. In the file, define and call a function called `main` that does the following:

* Creates a directory called `CyberSecurity-Notes` in the current working directory
* Within the `CyberSecurity-Notes` directory, creates 24 sub-directories (sub-folders), called `Week 1`, `Week 2`, `Week 3`, and so on until up through `Week 24`
* Within each week directory, create 3 sub-directories, called `Day 1`, `Day 2`, and `Day 3`

> Solution:
```python
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
```
> Output:
```python
    tree ./CyberSecurity-Notes/
    ./CyberSecurity-Notes/
    ├── Week_01
    │   ├── Day_1
    │   ├── Day_2
    │   └── Day_3
    :
    :
    └── Week_24
        ├── Day_1
        ├── Day_2
        └── Day_3
```

**Bonus Challenge**: Add a conditional statement to abort the script if the directory `CyberSecurity-Notes` already exists.

---

## Copying Student Exercises

So far you've used a few different Python modules, but for the rest of the homework, you will need to familiarize yourself with a new one. The `shutil` module is a Python module used for high-level file operations like moving and copying. Read [this beforehand](https://www.journaldev.com/20536/python-shutil-module) to get familiar with `shutil` and make sure to use the [documentation](https://docs.python.org/3.5/library/shutil.html#module-shutil) while you're working through the homework. 

Create a script called `copy_activities.py` with a function called `stu_activities` that does the following:

* Finds files in `~/Downloads` that contain the string `Stu_`
* Copies these files into the current working directory

**Note**: This isn't just a challenge to complete for the sake of it, this is a practical script you can run to move any downloaded files from class into your class notes directories.
> solution:
```python
import os
import glob
import shutil


def stu_activities(src_directory, dst_directory):
    """
    function stu_activities is to perform the following activities:
    * Finds files in ~/Downloads that contain the string Stu_
    * Copies these files into the current working directory

    :param src_directory: Source Directory
    :type src_directory:  Raw String
    :param dst_directory: Destination Directory
    :type dst_directory: Raw String
    :return: Number of files copied
    :rtype: int
    """
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
    return file_counter


if __name__ == "__main__":
    stu_activities(r"/Users/vsiddaia/Downloads/", r"./CyberSecurity-Notes")
```
---

## Copy Class Slides

Create a script called `copy_slides.py` with a function called `pptx_copy`
Students will create a script that does the following:

* Finds files in `~/Downloads` with the file extension `.pptx` or `.ppt`
* Copies these files into the current working directory

**Note**: This is another practical script you can use to move downloaded slides from class into your class notes directories.

> Solution:

```python
import os
import glob
import shutil


def pptx_copy(src_directory=".", dst_directory="."):
    """

    :param src_directory: Source Directory
    :type src_directory: raw string/path
    :param dst_directory: Destination Directory
    :type dst_directory: raw string/path
    :return: Number of files copied
    :rtype: integer
    """
    counter = 0
    for src_file in glob.glob(src_directory + os.sep + '**/*.ppt*', recursive=True):
        dst_file = dst_directory + os.sep + os.path.basename(src_file)
        try:
            shutil.copyfile(src_file, dst_file)
            counter +=1
        except shutil.SameFileError:
            print("Source and Destination are same !!!")
            break
        except:
            print("Un known Error in copying!!!")
    print(f"{counter} file(s) copied.")
    return counter


if __name__ == "__main__":
    pptx_copy(r"/Users/vsiddaia/Downloads/", r"./CyberSecurity-Notes")

```

> Output On Success:
```
15 file(s) copied.
```

> Output On Success:
```
Source and Destination are same !!!
0 file(s) copied.
```
---

## Updating PATH and Add an Alias

**Note**: Consider this a _bonus_. You do _not_ need to complete this step for credit. But, these tools will come up in class later, so you're strongly encouraged to study up now!

Now these great scripts have been written, but they are only executable from their relative path - where the files are in your system. In this final step, we'll make them accessible to you anywhere in your system directory.

* First, read the [following article](http://linuxcommand.org/lc3_wss0020.php) to learn more about `.bashrc`, `PATH`, aliases, and the `export` command and answer the following questions.
    * What is the main difference betweeen `~/.bashrc` and the `~/.bash_profile`?
    * What does the `export PATH` command do?
    * What is the benefit of creating aliases?
* Create a directory called `/usr/local/bin` and move your three scripts into this directory.
* Update your `.bashrc` to add the directory `/usr/local/bin` to `PATH` with the following command:

```
export PATH=$PATH:/usr/local/bin
```

* Finally create aliases in `.bashrc` for the three scripts
    * `alias copy_activities="copy_activities.py"`
    * `alias copy_slides="copy_slides.py"`
    * `alias create_notes_drs="create_notes_drs.py"`
> Solution:
```bash
    alias create_notes_drs=~/UT_CyberSecurity/Homework/GIT/CyberSecurity/Homework_04/create_notes_drs.py
    alias copy_slides=~/UT_CyberSecurity/Homework/GIT/CyberSecurity/Homework_04/copy_slides.py
    alias copy_notes=~/UT_CyberSecurity/Homework/GIT/CyberSecurity/Homework_04/copy_notes.py
```
## Submission
Please submit `create_notes_drs.py`, `copy_slides.py`, and `copy_notes.py`.
