# Hash Magic

## Solutions

Refer to [haystack.py](haystack.py) and [av.py](av.py) for the solution code.

To test `av.py`, pass the following paths for the malware and target directory, respectively:
- **Malware**: `./Resources/ls.exe`
- **Target Directory**
  - **Windows**: `C:/Program Files/Git/usr/bin`
  - **Mac**: `/usr/bin`

The script should hang for a second, and eventually identify `ls` as the "malware".

`ls` obviously isn't malware, but this scanner _would_ work if you passed it a real virus!
