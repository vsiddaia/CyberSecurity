## Unit 2 Homework Assignment: Keys to My Command Line

In this homework assignment, you will be using the concepts you've learned in class to complete **2 out of 3** Command-Line Challenges. 

Each of these challenges encompass a real-world situation where your new scripting skills will come in handy. 

Good luck! 

### Before You Begin

1. From within your Google Drive, create a folder called **02-Terminal_Challenge**. 

2. Right-click the **02-Terminal_Challenge** folder and select **Get Shareable Link**. You will use this folder to submit your homework when complete and the folder needs to be shareable so we can access it.

3. Inside your **02-Terminal_Challenge** folder, include two subfolders, one for each of the assignments.

## Challenge 1: Picture Tracker![alt text](https://github.com/vittalsiddaiah/CyberSecurity/blob/master/Homework_02/03-Images.jpg)

In this challenge, you've been given a zipped file (Pictures.zip) filled with folders of images. Your job is to create a shell script to complete the following:

* Create three folders called: **JPG**, **PNG**, **TIFF**.
* Locate all **.jpg**, **.png**, and **.tiff** files inside the folder and copy each into their respective folder. 

### ++**Solution library :**++ **verifyFileCount**
> Ensure to change to executable mode : ``` chmod +x verifyFileCount ```

```shell
#!/bin/bash
set -o noglob
# Verification 
# Function Count Files
# Usage:
#     countFiles <folder> <filetype>
countFiles ()	{
	printf `find $1 -iname $2 | wc -l`
	return `find $1 -iname $2 | wc -l`
}

# Function Count Files
# Usage:
#     verifyFileCount <folder1> <folder2> <filetype>
lhs=$(countFiles $1 $3)
rhs=$(countFiles $2 $3)
if [ $lhs == $rhs ]
	then 
		printf "$lhs Files Copied from $1 to $2 Successfully..." 
	else 
		printf "Error in Copying All/Some $3 Files !!!" 
fi

```



### ++**Solution:**++ **hw2_challenge1.sh**
> Ensure to change to executable mode : ``` chmod +x hw2_challenge1.sh ```
```shell
#!/bin/bash
set -o noglob
#Cleanup
rm -rf ./Pictures ./JPG ./PNG ./TIFF ./PictureCounts.md

# Code
SEP="-------------------------------------------------------\n"
# Unzipping 
printf "\b$SEP\t Unzipping Files ...\n"
unzip ./Pictures.zip 
printf "... Done \n$SEP"

# Creating Folders
mkdir JPG PNG TIFF

# Find files and copy
printf "\b$SEP\t Copying Files ..."
find ./Pictures -iname "*.jpg" -exec cp {} ./JPG \;
find ./Pictures -iname "*.png" -exec cp {} ./PNG \;
find ./Pictures -iname "*.tiff" -exec cp {} ./TIFF \;
printf "... Done \n$SEP"


# Verification Phase 
printf "\b$SEP\t Verifying Copy ...\n"
echo "### Picture assortion log:" > PictureCounts.md
printf " $SEP" | tee -a PictureCounts.md
echo "1. Verifying JPG Files : "   `./verifyFileCount ./Pictures ./JPG/  *.jpg`  | tee -a PictureCounts.md
echo "2. Verifying PNG Files : "   `./verifyFileCount ./Pictures ./PNG/  *.png`  | tee -a PictureCounts.md
echo "3. Verifying TIFF Files : "  `./verifyFileCount ./Pictures ./TIFF/ *.tiff` | tee -a PictureCounts.md
printf " $SEP" | tee -a PictureCounts.md
```



* Create a new file called **PictureCounts.md**.
* Count how many times each file type occurs and log the results to the **PictureCounts.md** file. 

### ++**Output File:**++

``` shell
cat ./PictureCounts.md 
### Picture assortion log:
 -------------------------------------------------------
1. Verifying JPG Files :  13 Files Copied from ./Pictures to ./JPG/ Successfully...
2. Verifying PNG Files :  10 Files Copied from ./Pictures to ./PNG/ Successfully...
3. Verifying TIFF Files :  8 Files Copied from ./Pictures to ./TIFF/ Successfully...
 -------------------------------------------------------
```
Your final submission should come in the form of: 

* A shell script (**.sh** file) with each of the commands with a comment above. Add a comment above each command describing the action.  

* An annotated PDF document with screenshots of each of the commands being run in the command line and the results shown in the file explorer when relevant. 

## Challenge 2: VIP Customers ![alt text](https://github.com/vittalsiddaiah/CyberSecurity/tree/master/Homework_02/01-VIP.jpg)
In this challenge, you are given a zip file (OrderRecords.zip) filled with Order and Inventory Records from 2012–2017. Your task is to create and run a shell script to complete the following:

1. Create a folder called **AllRecords**. 

2. Copy all of the order records from 2012–2017 into the **AllRecords** folder. 

3. Inside of the **AllRecords** folder, create a folder called **VIPCustomerOrders**.



```shell
mkdir -p -v ./AllRecords/VIPCustomerOrders
```


4. Find all orders from the VIP Customers Michael Davis or Michael Campbell. Include line and file names in the output.


5. Move these specific files into the **VIPCustomerOrders** folder in the form of two files: **michael_campbell_orders.output** and **michael_davis_orders.output**.



```shell
grep "Michael"  -ris ./OrderRecords/* | grep  "Davis"  > ./AllRecords/VIPCustomerOrders/michael_davis_orders.output
grep "Michael"  -ris ./OrderRecords/* | grep  "Campbell"  > ./AllRecords/VIPCustomerOrders/michael_campbell_orders.output
```

6. Create a file called **VIPCustomerDetails.md** that details how many orders each of the two users made. 


```shell
echo "Summary" > VIPCustomerDetails.md
echo "Michael Davis has" `cat  ./AllRecords/VIPCustomerOrders/michael_davis_orders.output |wc -l ` " Record(s)" >> VIPCustomerDetails.md
echo "Michael Campbell has" `cat  ./AllRecords/VIPCustomerOrders/michael_campbell_orders.output |wc -l ` " Record(s)" >> VIPCustomerDetails.md
```

Your final submission should come in the form of: 

* A shell script (**.sh** file) with each of the commands. Add a comment above each command describing the action.  


### ++**Solution:**++ **hw2_challenge2.sh**
> Ensure to change to executable mode : ``` chmod +x hw2_challenge2.sh ```
```bash
#!/bin/bash
mkdir -p -v ./AllRecords/VIPCustomerOrders
grep "Michael"  -ris ./OrderRecords/* | grep  "Davis"  > ./AllRecords/VIPCustomerOrders/michael_davis_orders.output
grep "Michael"  -ris ./OrderRecords/* | grep  "Campbell"  > ./AllRecords/VIPCustomerOrders/michael_campbell_orders.output
echo "Summary" > VIPCustomerDetails.md
echo "Michael Davis has" `cat  ./AllRecords/VIPCustomerOrders/michael_davis_orders.output |wc -l ` " Record(s)" >> VIPCustomerDetails.md
echo "Michael Campbell has" `cat  ./AllRecords/VIPCustomerOrders/michael_campbell_orders.output |wc -l ` " Record(s)" >> VIPCustomerDetails.md

```

### ++**Output File:**++
```shell
cat ./VIPCustomerDetails.md 
Summary
Michael Davis has 5  Record(s)
Michael Campbell has 1  Record(s)
```


## Challenge 3: To-Do Counter ![alt text](https://github.com/vittalsiddaiah/CyberSecurity/tree/master/Homework_02/02-Todo.jpg)
In this challenge, you've been given zip file (Todos.zip) that includes a set of folders related to three coworkers' to-do lists. Each coworker's to dos are included in their respective folder. Your job is to create a shell script to complete the following:

1. Within each of the folders, create an **all.txt** file that combines the to dos included in the individual's to-do lists.

2. Within each of the folders, create a file called **done.txt** that includes only to dos marked as done.

3. Within each of the folders, create a file called **unfinished.txt** that includes only to dos not marked as done.

4. Create a file called **ProductivityReport.md** at the base of the **Todos** folder that specifies the number of to dos each person completed and the number they have left. **Note:** Because of the complexity of this activity, you do not need to use the script to print your results to the ProductivityReport, but you must use a script to do the counting.

5. Your final **ProductivityReport.md** might look something like the following:

    ```
    Done:
    Carrie: 12
    Jennifer: 3
    John: 8
    
    To Still Do:
    Carrie: 1
    Jennifer: 9
    John: 2
    
    ```

Your final submission should come in the form of: 

* A shell script (**.sh** file) with each of the commands with a comment above. Add a comment above each command describing the action.  

* An annotated PDF document with screenshots of each of the commands being run in the command line and the results shown in the file explorer when relevant. 

### ++**Solution:**++ **hw2_challenge3.sh**
> Ensure to change to executable mode : ``` chmod +x hw2_challenge3.sh ```
```bash
#!/bin/bash
#!/bin/bash
unzip -o ./Todos.zip

_doneList=`printf "Done:\n" `
_todoList=`printf "To Still Do:\n" `

for _name in Carrie Jennifer John
do
	_all=`find ./Todos/$_name/ -type f -iname "*todos*" -exec cat {} \; |wc -l |xargs`
	_done=`find ./Todos/$_name/ -type f -iname "*todos*" -exec cat {} \; | grep -ris done |wc -l|xargs`
	_doneList=`printf "$_doneList \n $_name: $_done"`
	_todoList=`printf "$_todoList \n $_name: $((_all - _done))"`
done

printf "$_doneList\n\n" > ProductivityReport.md 
printf "$_todoList\n" >> ProductivityReport.md 
```

### ++**Output File:**++
```shell
cat ./ProductivityReport.md 
Done: 
 Carrie: 6 
 Jennifer: 2 
 John: 3

To Still Do: 
 Carrie: 7 
 Jennifer: 2 
 John: 3
```

-----

## Copyright

Trilogy Education Services © 2018. All Rights Reserved.
