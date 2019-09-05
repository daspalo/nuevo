sex = input("are you a male or female?(M or F) ")
age = float(input("What is your age?" ))

if not sex == "M" and not age >= 65:
    print("male senior citizen")

elif not sex == "F" and not age >= 65:
    print("female senior citizen")

else:
    print("must be relatively young")
