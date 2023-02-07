#calculating bonus by using years of service

salary = float(input("Enter your salary: "))
years_of_service = float(input("Enter your years of service: "))

if years_of_service > 10:
    bonus = salary * 0.1
elif years_of_service >= 6 and years_of_service <= 10:
    bonus = salary * 0.08
else:
    bonus = salary * 0.05

net_bonus = salary + bonus
print("Your net bonus amount is:", net_bonus)
