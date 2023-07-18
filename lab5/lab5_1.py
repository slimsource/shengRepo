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
from datetime import datetime


def print_program_info():
    name = "Sheng Lim"
    lab_name = "Lab 5 - File Counters"
    current_time = datetime.now()
    current_time_in_request_format = current_time.strftime("%b-%d-%Y %a (%I:%M:%S%p)")

    print("{:16}".format("Name"), ":", "CNET-142", name)
    print("{:16}".format("Lab"), ":", lab_name)
    print("{:16}".format("Current Time"), ":", current_time_in_request_format)


def ask_user_filename():
    return input("What's the input filename? :")


def read_file(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        return lines  # Return a list with content
    except IOError:
        print("Error: can't open file", filename)
        return []   # Return an empty list


def print_lines(lines):
    for i, line in enumerate(lines, 1):
        line = line.strip()
        print(f"Line {i}: {line}")


def count_lines(lines):
    num_lines = len(lines)
    print("Total number of lines:", num_lines)


def count_words(lines):
    word_count = 0
    for line in lines:
        words = line.strip().split()
        word_count += len(words)
    print("Total number of words:", word_count)


def count_characters(lines):
    char_count = sum(len(line) for line in lines)
    print("Total number of characters:", char_count)


def count_uppercase_letters(lines):
    uppercase_count = sum(char.isupper() for line in lines for char in line)
    print("Total number of uppercase letters:", uppercase_count)


def count_lowercase_letters(lines):
    lowercase_count = sum(char.islower() for line in lines for char in line)
    print("Total number of lowercase letters:", lowercase_count)


def count_spaces(lines):
    space_count = sum(char.isspace() for line in lines for char in line)
    print("Total number of spaces:", space_count)


def count_digits(lines):
    digit_count = sum(char.isdigit() for line in lines for char in line)
    print("Total number of digits:", digit_count)


def count_sentences(lines):
    sentence_count = sum(1 for line in lines for char in line if char in ('.', '!', '?'))
    print("Total number of sentences:", sentence_count)


def ask_user_input_filename_and_start_from_here():
    filename = ask_user_filename()
    lines = read_file(filename)

    if lines:
        print_lines(lines)
        count_lines(lines)
        count_words(lines)
        count_characters(lines)
        count_uppercase_letters(lines)
        count_lowercase_letters(lines)
        count_spaces(lines)
        count_digits(lines)
        count_sentences(lines)


def main():
    print_program_info()
    ask_user_input_filename_and_start_from_here()


if __name__ == "__main__":
    main()
