def calculate_compound_interest(principle, interest_rate, compound_frequency, years):
    amount = principle * (1 + (interest_rate / compound_frequency)) ** (compound_frequency * years)
    return amount

principle = float(input("Enter the principle amount: "))
interest_rate = float(input("Enter the interest rate (in decimal, exp 2.75=0.0275): "))
compound_frequency = int(input("Enter the number of times the interest is compounded per year: "))
years = int(input("Enter the number of years the account will earn interest: "))

final_amount = calculate_compound_interest(principle, interest_rate, compound_frequency, years)

rounded_final_amount = round(final_amount,2)

print("The final amount after {} years is: {}".format(years, rounded_final_amount))
