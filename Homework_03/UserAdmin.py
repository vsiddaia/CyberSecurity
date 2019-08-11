import pprint
import string
import secrets
import getpass


def set_dataset(self):
    '''
    function to initialize the data set
    Returns userInfo and adminList
    -------
    '''
    allChars = string.ascii_letters + string.digits + string.punctuation
    userInfo = []
    for x in range(10):
        passwd = ''
        for y in range(10): passwd += secrets.choice(allChars)
        userInfo.append({"username": "User_" + str(x), "password": passwd})
    adminList = [
        {
            "username": "DaBigBoss",
            "password": "DaBest"
        },
        {
            "username": "root",
            "password": "toor"
        }
    ]
    userInfo.append(adminList[0])
    userInfo.append(adminList[1])
    return [userInfo, adminList]


def getCreds(self):
    uname = input("username : ")
    maxTrial = 3
    trial = 0
    is_login_successful = False
    while trial < maxTrial:
        pswd = getpass.getpass()
        is_ok = False
        for user in userInfo:
            if (user["username"].upper() == uname.upper()) and (user["password"] == pswd.strip()):
                pprint.pprint(userInfo)
                is_ok = True;
                break
        if not is_ok:
            print("Incorrect password !!!, Please try again ...")
            trial += 1
        else:
            is_login_successful = True
            break
    if not is_login_successful:
        print("Sorry max'd out on trials please try after some time.")
    else:
        print("Login Successful...")


[userInfo, adminList] = set_dataset()
getCreds()
