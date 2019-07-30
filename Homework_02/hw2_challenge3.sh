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

