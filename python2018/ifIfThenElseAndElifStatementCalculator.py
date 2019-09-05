print("This calculator allows the user to enter two numbers and the user to choose the type of operation to perform")
numb1 = int(input("Enter a Number: "))
numb2 = int(input("Enter another number: "))

val= input("Enter the mathematical operation to perform (options: + - * /):")

if val == '+':
    print(numb1,"+",numb2,"=", numb1 + numb2)

elif val == '-':
    print(numb1,"-",numb2,"=", numb1 - numb2)

elif val == '*':
    print(numb1,"*",numb2,"=", numb1 * numb2)

elif val == '/':
    print(numb1,"/",numb2,"=", numb1 / numb2)

else:
    print("Operation could not be recognized")
