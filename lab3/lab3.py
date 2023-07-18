#-------------------------------------------------
# Program Name: lab3.py
# Program Description:
# This program calcuates the total amount of principle plus interset compounded  
# over a number of years.
#        
# total = p*(1+(r/100)/n)**(n*t)
# interest=total-p
# p is initial principle
# r is the annual interest rate
# n is how many times the intestest compounds in a year
# t is the number of years that the account earns interest
#
# @Author: Sheng Lim
# @Date: 7/1/2023
#----------------------------------------------
from datetime import datetime

name="Sheng Lim"
lab_name="Lab 3 -  Interest Rate"
current_time=datetime.now() 
current_time_in_request_format=current_time.strftime("%b-%d-%Y %a (%I:%M:%S%p)")

print("{:16}".format("Name"),":", "CNET-142", name)
print ("{:16}".format("Lab"), ":", lab_name)          
print("{:16}".format("Current Time"), ":", current_time_in_request_format)

while True:
    p=float(input("Enter the starting principal, 0 to quit: "))
    if p<=0:
        break
    r=float(input("Enter the annual interest rate: "))
    n=int(input("How many times per year is the interest commpunded? "))
    t=int(input("For how many years will the account earn interest? "))
    
    total=p*(1+(r/100)/n)**(n*t)
    #total_1='{0:.2f}'.format(total)  This one works but too lenghty
    total_1= round(total,2)
    interest=total-p
    #interest_1='{0:.2f}'.format(interest)  This one works but too lenghty
    interest_1= round(interest,2)

    print("At the end of",t,"years you will have $",total_1,"with interest earned $",interest_1)






