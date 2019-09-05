print("This calculator allows the user to enter two numbers and the user to choose the type of operation to perform")
number_1 = int(input("Enter a Number: "))
number_2 = int(input("Enter another number: "))
operation = input("Enter the mathematical operation to perform '(Options: + - * /)': ")
if operation == " + ":
    print(" {} + {} = " .format(number_1, number_2))
    print(number_1 + number_2)

elif operation == " - ":
    print(" {} - {} = " .format(number_1, number_2))
    print(number_1 - number_2)
    
elif operation == " * ":
    print(" {} * {} = " .format(number_1, number_2))
    print(number_1 * number_2)

elif operation == " / ":
    print(" {} / {} = " .format(number_1, number_2))
    print(number_1 / number_2)

else:
    print("Operation could not be recognized")

    
  
          
          
