# Verification 

# Function Count Files
# Usage:
#     countFiles <folder> <filetype>
countFiles ()	{
	return `find $1 -iname $2 | wc -l`
}

# Function Count Files
# Usage:
#     verifyFileCount <folder1> <folder2> <filetype>
verifyFileCount()	{
	echo $1 $2 $3
	lhs=`countFiles $1 $3`
	rhs=`countFiles $2 $3`
	if [ $lhs == $rhs ]
	then
		echo "Files Copied Successfully..." 
	else 
		echo "Error in Copying !!!" 
	fi
	return
}