citizenship= input("Are you a Kenyan citizen (YES/NO)? ")
age = int(input("Enter your age? "))

if citizenship == "yes" and age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
