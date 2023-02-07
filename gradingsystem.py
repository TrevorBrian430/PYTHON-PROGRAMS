unit1 = int(input("Enter score for unit 1: "))
unit2 = int(input("Enter score for unit 2: "))
unit3 = int(input("Enter score for unit 3: "))
avg = (unit1 + unit2 + unit3) / 3
  
if avg >= 70 and avg <= 100:
  print("Your grade is A")
elif avg >= 60 and avg <= 69:
  print("Your grade is B")
elif avg >= 50 and avg <= 59:
  print("Your grade is C")
elif avg >= 40 and avg <= 49:
  print("Your grade is D")
elif avg >= 0 and avg <= 39:
  print("Your grade is Fail")

