#!/usr/bin/python
# -------------------------------------------------#
# Match first and last word and say True or False
# Here we try to see the sentence is that It starts
# with the word "The", then bla, bla, bla, then ends
# with the word "Spain".
# --------------------------------------------------#
import re

txt = "The rain in Spain"

x = re.search("^The.*Spain$", txt)  # This line returns TRUE or FALSE, "." any character, "*" zero or more occurrence.

if x:
	print("Yes, We have a match!")
else:
	print("No match!")





