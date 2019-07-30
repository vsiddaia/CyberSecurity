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

