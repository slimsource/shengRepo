#-------------------------------------------------
# Program Name: lab2.py
# Program Description:
#     See Below
#        
#     
#
# @Author: Sheng Lim
# @Date: 6/25/2023
#
#----------------------------------------------
# INPUT
#----------------------------------------------
# The program asked the user to enter below:
#
# 1. Car gas tank’s capacity in gallons.
# 2. Gas mileage per gallon (MPG) 
# 3. Gas price per gallon.
#
#--------------------------------------------
# FORMULAS
#--------------------------------------------
# There are 2 formulas we can use:
#
# 1. Cost of driving 100 miles =100/Mileage x Price
#
# For example, if the car runs 20 miles per gallon, each gallon costs $5.
# That means, $5 can go 20 miles. Then $25 can go 100 miles. 
#
# Let’s verify with the formula: 
# To run 100 miles, the cost is 100/20 x 5 =$25 
# 
# 2. Distance=Capacity x Gas Mileage 
#
# if the tank capacity is 10 gallons.  Each gallon can go 20 miles.
# The distance = 10 x 20 = 200 miles. 
#
#--------------------------------------------------
# OUTPUT
#---------------------------------------------------
#The program will print out below:
#
# 1. Cost for driving 100 miles. 
# 2. Distance of full tank can go. 
# 3. Tell how efficient the car is, based on below conditions: 
#    1. MPG less than 30, “Not efficient”.
#    2. MPG between 30 and 40, “Average”.
#    3. MPG between 40 and 50, “Efficient”.
#    4. MPG greater than 50, “Very Efficient”.
#---------------------------------------------------------------------------------
from datetime import datetime

name="Sheng Lim"
lab_name="Lab 2 - Car Mileage"
current_time=datetime.now() 
current_time_in_request_format=current_time.strftime("%b-%d-%Y %a (%I:%M:%S%p)")


print("{:16}".format("Name"),":", "CNET-142", name)
print ("{:16}".format("Lab"), ":", lab_name)          
print("{:16}".format("Current Time"), ":", current_time_in_request_format)


# Obtain User Inputs
gas_tank_capacity = float(input("Enter the capacity of the car's gas tank (in gallons):"))
mpg= float(input("Enter car's miles per gallon:"))
gas_price_per_gallon= float(input("Enter price per gallon:"))

cost_per_100_miles = round(100/mpg*gas_price_per_gallon,2)

distance_per_full_tank= round(gas_tank_capacity*mpg, 2)

# Calculate the car's efficiency 
if mpg < 30:
    efficiency = 'It\'s not fuel efficient car.'
elif mpg < 40:
    efficiency = 'It\'s average fuel efficient car.'
elif mpg < 50:
    efficiency = 'It\'s fuel efficient car.'
else:
    efficiency = 'It\'s very fuel efficient car'


# Print the result 
print("Cost for driving 100 miles is $", cost_per_100_miles)
print("Distance on a tank of gas is", distance_per_full_tank)
print("Your car MPG is", mpg, efficiency)





























