from datetime import datetime

name="Sheng Lim"
lab_name="Lab 4 -  Functions"
current_time=datetime.now() 
current_time_in_request_format=current_time.strftime("%b-%d-%Y %a (%I:%M:%S%p)")

print("{:16}".format("Name"),":", "CNET-142", name)
print ("{:16}".format("Lab"), ":", lab_name)          
print("{:16}".format("Current Time"), ":", current_time_in_request_format)

def Calculate_Simple_Interest():

    while True:
        p=float(input("Enter the starting principal, 0 to quit: "))
        if p<=0:
            print("OK, you've decided to quit the program.")
            break
        r=float(input("Enter the annual interest rate: "))
        n=int(input("How many times per year is the interest compounded? "))
        t=int(input("For how many years will the account earn interest? "))
    
        total=p*(1+(r/100)/n)**(n*t)
        total_1 = str(round(total, 2))
        interest=total-p
        interest_1 = str(round(interest, 2))

        print("At the end of",t,"years you will have $",total_1,"with interest earned $",interest_1)

def Calculate_Mortgage_Payment():

    while True:
        p=float(input("Enter the loan amount, 0 to quit: "))
        if p<=0:
            print("OK, you've decided to quit the program.")
            break
        r=float(input("Enter the loan interest rate: "))
        n=int(input("Enter the loan term (number of years)"))

    monthlyRate = (r/100)/12 
    numPayments = n*12
    monthlyPayment = p*(monthlyRate/(1-(1+monthlyRate)**numPayments))
    rounded_monthlyPayment = round(monthlyPayment, 2)
    totalAmount = monthlyPayment*12*n
    rounded_totalAmount = round(totalAmount, 2)
    interestPaid = totalAmount - p
    rounded_interestPaid = round(interestPaid, 2)

    print("For the loan Amount of ${} for {} years with interest rate of {} %").format(p,n,r)    
    print("The monthly payment is ${}").format(rounded_monthlyPayment)
    print("Total amount paid for this loan is ${}".format(rounded_totalAmount))
    print("Total interest paid for this loan is ${}".format(rounded_interestPaid))


def main():
    name="Sheng Lim"
    lab_name="Lab 4 -  Functions"
    current_time=datetime.now() 
    current_time_in_request_format=current_time.strftime("%b-%d-%Y %a (%I:%M:%S%p)")

