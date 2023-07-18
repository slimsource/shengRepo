# Program Name: lab1_new.py
# Program Description:
#     This program prints below
#        1. User's name
#        2. Lab name
#        3. Current Time
#
# @Author: Sheng Lim
# @Date: 6/18/2023

from datetime import datetime

name="Sheng Lim"
lab_name="Lab 1 - Print Name"
current_time=datetime.now() 
current_time_in_request_format=current_time.strftime("%b-%d-%Y %a (%I:%M:%S%p)")


print("{:16}".format("Name"),":", "CNET-142", name)
print ("{:16}".format("Lab"), ":", lab_name)          
print("{:16}".format("Current Time"), ":", current_time_in_request_format)