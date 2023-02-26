principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate as a decimal: "))
time = float(input("Enter the time period in years: "))
periods = int(input("Enter the number of times the interest is compounded per year: "))
def compound_interest():
    amount = principal * ((1 + (rate / periods)) ** (periods * time))
    interest = amount - principal

    print("The compound interest earned is:", interest)
compound_interest()