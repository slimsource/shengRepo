#!/bin/bash
#--------------------------------------------------------------------
# Enter a name and show if it is on the list or not
# Syntax: ./<script> <name>
#
# if-else-fi loop
# $?            : based on last user entry, return 0 if pass, 1 for fail 
# > /dev/null   : Hide output of command
#--------------------------------------------------------------------
grep $1 mailingList.txt > /dev/null # hide output

if [ $? -ne 0 ]; then
echo $1 'is NOT on the mailing list, Sorry!'
exit
else
echo $1 'is found on the mailing list.'
exit
fi
