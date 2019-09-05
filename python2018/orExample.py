sex = input("are you a male or female?(M or F) ")
age = float(input("What is your age?" ))

if sex == "M" or age >= 65:
    print("male senior citizen")

elif sex == "F" or age >= 65:
    print("female senior citizen")

else:
    print("must be relatively young")
