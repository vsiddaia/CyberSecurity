## Unit 3 Homework Assignment: Intro to Python Programming 

In this homework assignment, you will be using the concepts you've learned in class to complete the below two activities. 


---
## DNS Dictionary

As a network admin, you've been given a list of DNS server IPs and their providers in two separate lists. Your company needs these in an accessible form in order to verify the DNS server IP and provider together in case malware alters company machines' IP configurations to use a rogue DNS server.

In order to look up a DNS server IP using the provider name, you'll need to build a way to put that information together, similar to a phone book.

Your goal is to build different data structures for easily accessing information associated with these DNS properties.

### Instructions

Open up the `Unsolved/DNSDictionary.py` file. For each step, accomplish the following:

1. Use a `for` loop to create a dictionary mapping the provider names to their IPs.

   - For example, two entries in the dictionary would look like:

        ```python
        {
            'Level3': '209.244.0.3',
            'Verisign': '64.6.64.6'
        }
        ```

> Solution:
 
```python
        ipDict = {}
        if(len(providers) == len(ips)):
            for idx in range(len(ips)):
                ipDict.update({providers[idx]:ips[idx]})
```
> Output:

```
        [{'provider_name': 'Level3', 'provider_server': '209.244.0.3'},
         {'provider_name': 'Verisign', 'provider_server': '64.6.64.6'},
         {'provider_name': 'Google', 'provider_server': '8.8.8.8'},
         {'provider_name': 'Quad9', 'provider_server': '9.9.9.9'},
        :
        :
         {'provider_name': 'puntCAT', 'provider_server': '109.69.8.51'},
         {'provider_name': 'Neustar', 'provider_server': '156.154.70.1'},
         {'provider_name': 'Cloudflare', 'provider_server': '1.1.1.1'},
         {'provider_name': 'Fourth Estate', 'provider_server': '45.77.165.194'}]
```


   - Print Hurricane Electric's IPs using the dictionary.

> Solution:

```python
        ipDict["Hurricane Electric"]
```
> Output:

``` 
        '74.82.42.42' 
```


2. Use a `for` loop to create a list of dictionaries with the associated information.

   - For example, two entries in the list would look like:

        ```python
        [
            {
                'provider_name': 'Level3',
                'primary_server': '209.244.0.3'
            },
            {
                'provider_name': 'Verisign',
                'primary_server': '64.6.64.6'
            }
        ]
        ```
    > Solution:

    ```python
        ipList=[]
        for key, value in ipDict.items():
            ipList.append({'provider_name': key, 'provider_server': value})
        ipList
    ```
    > Output:
    ```
        [{'provider_name': 'Level3', 'provider_server': '209.244.0.3'},
        {'provider_name': 'Verisign', 'provider_server': '64.6.64.6'},
        {'provider_name': 'Google', 'provider_server': '8.8.8.8'},
        :
        :
        {'provider_name': 'Cloudflare', 'provider_server': '1.1.1.1'},
        {'provider_name': 'Fourth Estate', 'provider_server': '45.77.165.194'}]
    ```
   
   - Print the total number of providers using the list.

> Solution:

```python
        print("Total Number of Providers : %d" % len(ipList))
```
> Output:
```
        Total Number of Providers : 22
```

### Bonuses

1. Use a `for` loop to update your dictionary from part 1 with the new IPs.

   - For example, two entries in the dictionary would look like:

        ```python
        {
            'Level3': ['209.244.0.3', '209.244.0.4'],
            'Verisign': ['64.6.64.6', '64.6.65.6']
        }
        ```
   - The IPs should be in the form of an array of IPs.

> Solution:

```python
        for sip in secondary_ips:
            ipDict[sip['provider']] = [ipDict[sip['provider']], sip['ip']]
```

 > Output:

```
        {'Level3': ['209.244.0.3', '209.244.0.4'],
         'Verisign': ['64.6.64.6', '64.6.65.6'],
        :
         'Cloudflare': ['1.1.1.1', '1.0.0.1'],
         'Fourth Estate': '45.77.165.194'}
```
   - Print Google's IPs using the dictionary.

> Solution:

```python
        ipDict['Google']
```
> Output:

```
        ['8.8.8.8', '8.8.4.4']
```

2. Use nested `for` loops to update the list from part 2 with a `'secondary_server'` key.

   - For example, two entries in the list would look like:

        ```python
        [
            {
                'provider_name': 'Level3',
                'primary_server': '209.244.0.3',
                'secondary_server': '209.244.0.4'
            },
            {
                'provider_name': 'Verisign',
                'primary_server': '64.6.64.6',
                'secondary_server': '64.6.65.6'
            }
        ]
        ```

3. Super Bonus: use the `pprint` module to print the dictionary and list more elegantly. This will take a lot of research, but we will cover this in a future class.
> Solution:
```python
pp = pprint.PrettyPrinter(width=40, compact=True)
pp.pprint(ipList)
pp.pprint(ipDict)
```

> Output:

```
        [{'provider_name': 'Level3',
          'provider_server': '209.244.0.3'},
         {'provider_name': 'Verisign',
          'provider_server': '64.6.64.6'},
         {'provider_name': 'Google',
          'provider_server': '8.8.8.8'},
          :
          :
          {'provider_name': 'Fourth Estate',
          'provider_server': '45.77.165.194'}]

         {'Alternate DNS': '198.101.242.72',
         'Cloudflare': '1.1.1.1',
         :
         :
         'Yandex.DNS': '77.88.8.8',
         'puntCAT': '109.69.8.51'} 
```

---

## UserAdmin

When you buy a new home WiFi router, it typically comes with one admin login and password to access settings via the product's website. If you don't have this admin password, you're unable to change things like the WiFi network name and password. 

In this activity, you'll use Python to build a login system for a WiFi router that only allows those with admin credentials to log in.

### Instructions

1. Open up `Unsolved/UserAdmin.py`.

> Solution:
```python
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
``` 

> Output:

```
        [{'username': 'User_0', 'password': '7FEbQ#4$5l'},
         {'username': 'User_1', 'password': '=m|va$V^y$'},
         {'username': 'User_2', 'password': '\\>D=|#3ag?'},
         {'username': 'User_3', 'password': "`AK'U$xU[x"},
         {'username': 'User_4', 'password': "a'HGf\\jmp+"},
         {'username': 'User_5', 'password': 'RNt<Oh-~"~'},
         {'username': 'User_6', 'password': 'xCfHSG4.t+'},
         {'username': 'User_7', 'password': 'TO:m"jA>AD'},
         {'username': 'User_8', 'password': ')qZ}L#X{.L'},
         {'username': 'User_9', 'password': 'RH3^.#@JYj'},
         {'username': 'DaBigBoss', 'password': 'DaBest'},
         {'username': 'root', 'password': 'toor'}]
```

2. Create a function named `getCreds` with no parameters that will prompt the user for their username and password. This function should return a dictionary called `userInfo` that looks like the dictionaries below:

```python
# Administrator accounts list
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
```

> Solution:
```python
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
```


> Output:

```
        [{'password': '7FEbQ#4$5l', 'username': 'User_0'},
         {'password': '=m|va$V^y$', 'username': 'User_1'},
         {'password': '\\>D=|#3ag?', 'username': 'User_2'},
         {'password': "`AK'U$xU[x", 'username': 'User_3'},
         {'password': "a'HGf\\jmp+", 'username': 'User_4'},
         {'password': 'RNt<Oh-~"~', 'username': 'User_5'},
         {'password': 'xCfHSG4.t+', 'username': 'User_6'},
         {'password': 'TO:m"jA>AD', 'username': 'User_7'},
         {'password': ')qZ}L#X{.L', 'username': 'User_8'},
         {'password': 'RH3^.#@JYj', 'username': 'User_9'},
         {'password': 'DaBest', 'username': 'DaBigBoss'},
         {'password': 'toor', 'username': 'root'}]
```


3. Create a function named `checkLogin` with two parameters: the `userInfo` and the `adminList`. The function should check the credentials to see if they are contained within the admin list of logins. The function should set a variable `loggedIn` to `True` if the credentials are found in the admin list, and set the variable to `False` otherwise.

Now that we know how to check to see if a user is logging in with admin credentials, let's set up the part of the system that will continue to prompt the user for their username and password if they didn't enter correct admin credentials before. 


> Solution:
```python
    import pprint
    import string
    import secrets
    import getpass


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
``` 

> Output:[Successful Password]

```
    username : root
    Password: 
    [{'password': 'ke34BOkSq&', 'username': 'User_0'},
     {'password': '7x-O?lG*&R', 'username': 'User_1'},
     {'password': '`P/|zQ!p,Q', 'username': 'User_2'},
     {'password': '~rDfedS6j(', 'username': 'User_3'},
     {'password': ',5$"CrL=~@', 'username': 'User_4'},
     {'password': 'lG\\:g)3a2]', 'username': 'User_5'},
     {'password': 'scw;Oo1.(Q', 'username': 'User_6'},
     {'password': '!~5%9?^c(N', 'username': 'User_7'},
     {'password': '\\(X(Q[COg|', 'username': 'User_8'},
     {'password': '#2dK2}qSM"', 'username': 'User_9'},
     {'password': 'DaBest', 'username': 'DaBigBoss'},
     {'password': 'toor', 'username': 'root'}]
    Login Successful...
```

> Output:[Un-Successful Password]
```
        username : root
        Password: 
        Incorrect password !!!, Please try again ...
        Password: 
        Incorrect password !!!, Please try again ...
        Password: 
        Incorrect password !!!, Please try again ...
        Sorry max'd out on trials please try after some time.

```

4. Create a `while` loop that will continue to call `getCreds` and `checkLogin` until a user logs in with admin credentials. 

5. After each call of `checkLogin` in the `while` loop, print to the terminal the string `"---------"`.

6. Once the user logs in with admin credentials, print to the terminal the string `"YOU HAVE LOGGED IN!"`.

3. Run the code often as you write and test individual functions with correct and incorrect admin credentials to make sure you're on the right path!
