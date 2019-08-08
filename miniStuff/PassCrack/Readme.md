## Crack the password using **Brute Force Method**

> Solution:
```python
import os, glob, zipfile
dirPassword = "<YOUR PATH>/Passwords/"
zippedFiles = "<YOUR PATH>/ZippedFiles/"


def UnZipper(zipFile, passwd):
    try:
        with zipfile.ZipFile(zipFile) as fpZipFile:
            fpZipFile.extractall(pwd=bytes(passwd, 'utf-8'))
            return True
    except: return False


for zipFile in glob.glob(zippedFiles+"*.zip"):
    for passwordFile in glob.glob(dirPassword+"*.txt"):
        with open(passwordFile) as fpPassFile:
            for passwd in fpPassFile.readlines():
                if UnZipper(zipFile, passwd.strip()):
                    print(f"{os.path.basename(zipFile)}  {passwd.strip()}")

```

