import datetime

# Print name and current time
print("Name: Your Name")
print("Current Time:", datetime.datetime.now())

# Ask for user inputs
while True:
    principle = float(input("Enter principle amount (0 to exit): "))
    
    if principle <= 0:
        break
    
    rate = float(input("Enter annual interest rate: "))
    compound = int(input("Enter number of times interest is compounded in a year: "))
    years = int(input("Enter number of years: "))
    
    # Calculate ending total balance
    total = principle * (1 + float(rate / 100) / compound) ** (compound * years)
    interest = total - principle
    
    # Print the results with 2 decimal points
    print("Ending Total Balance:", "{:.2f}".format(total))
    print("Interest Earned:", "{:.2f}".format(interest))
    print()

print("Exiting the program.")
