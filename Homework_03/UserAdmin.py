import secrets
import string
import pprint
import getpass


def set_dataset():




    ''' set_dataset() takes no input arguments and returns two

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

def getCreds():
    uname = input("username : ")
    maxTrial = 3
    trial = 0
    isLoginSuccessful = False
    while trial < maxTrial:
        pswd = getpass.getpass()
        isOk = False
        for user in userInfo:
            if (user["username"].upper() == uname.upper()) and (user["password"] == pswd.strip()):
                pprint.pprint(userInfo)
                isOk = True;
                break
        if not isOk:
            print("Incorrect password !!!, Please try again ...")
            trial += 1
        else:
            isLoginSuccessful = True
            break
    if not isLoginSuccessful:
        print("Sorry max'd out on trials please try after some time.")
    else:
        print("Login Successful...")


[userInfo, adminList] = set_dataset()

getCreds()