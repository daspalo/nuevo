sex = input("are you a male or female?(M or F) ")
age = float(input("What is your age? "))

if sex == "M" and age >= 65:
    print("male and citizen")

elif sex == "F" and age >= 65:
    print("female and citizen")

else:
    print("must be relatively young")
    
