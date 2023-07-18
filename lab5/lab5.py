#-------------------------------------------------
# Program Name: lab5.py
# Program Description:
#  
#  This programs open and read a file, then calculates 
#  the total numbers of below:      
#  1. Lines
#  2. Words
#  3. Characters
#  4. Uppercase letters
#  5. Lowercase letters
#  6. Spaces
#  7. Digits
#  8. Sentences
#
# @Author: Sheng Lim
# @Date: 7/16/2023
#----------------------------------------------

import re
from datetime import datetime


def print_program_info():
    name = "Sheng Lim"
    lab_name = "Lab 5 - File Counters"
    current_time = datetime.now()
    current_time_in_request_format = current_time.strftime("%b-%d-%Y %a (%I:%M:%S%p)")

    print("{:16}".format("Name"), ":", "CNET-142", name)
    print("{:16}".format("Lab"), ":", lab_name)
    print("{:16}".format("Current Time"), ":", current_time_in_request_format)


def ask_user_input_filename_and_start_from_here():
    inputFileName = input("What's the input filename? :")
    outputFileName = "output_" + inputFileName

    try:
        with open(inputFileName, "r") as inFile:
            lines = inFile.readlines()

            for i, line in enumerate(lines, 1):
                line = line.strip()
                print(f"Line {i}: {line}")

            # Count the number of lines in the file
            num_lines = len(lines)
            if num_lines >= 0:
                print("Total number of lines:", num_lines)
            else:
                print("Something is wrong, please check the file.")

            # Count the number of words in the file
            word_count = 0
            for line in lines:
                words = line.strip().split()
                word_count += len(words)

            print("Total number of words:", word_count)

            # Count the number of characters in the file
            char_count = 0
            for line in lines:
                char_count += len(line)

            print("Total number of characters:", char_count)

            # Count the number of below in the file
            #  Uppercase letters
            #  Lowercase letters
            #  Space
            #  Digit
            #  Sentence (by counting '.' and '!' and '?')
              
            uppercase_count = 0
            lowercase_count = 0
            space_count = 0
            digit_count = 0
            sentence_count = 0

            for line in lines:
                for char in line:
                    if char.isupper():
                        uppercase_count += 1
                    elif char.islower():
                        lowercase_count += 1    
                    elif char.isspace():
                        space_count += 1
                    elif char.isdigit():
                        digit_count += 1
                    elif char in ('.', '!', '?'):
                        sentence_count += 1

            print("Total number of uppercase letters:", uppercase_count)            
            print("Total number of lowercase letters:", lowercase_count)            
            print("Total number of spaces:", space_count)            
            print("Total number of digits:", digit_count)            
            print("Total number of sentences:", sentence_count)

        # Close the file    
        inFile.close()            

    except IOError:
        print("Error: can't open file", inputFileName)


def main():
    print_program_info()
    ask_user_input_filename_and_start_from_here()


if __name__ == "__main__":
    main()
