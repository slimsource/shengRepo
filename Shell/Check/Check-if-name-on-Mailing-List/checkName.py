#!/bin/bash
#----------------------------------------------------
# Enter a name and show if it is on the list or not
# Syntax: ./<script> <name>
#----------------------------------------------------
grep $1 mailingList.txt > /dev/null #Do Not show the output of grep, redirect to /dev/null

if [ $? -ne 0 ]; then
echo $1 'is NOT on the mailing list, Sorry!'
exit
else
echo $1 'is found on the mailing list.'
exit
fi
