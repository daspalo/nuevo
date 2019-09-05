def DoTheMath(tmpFirstNum, tmpOperatorSym, tmpSecondNum):
    if(tmpOperatorSym == "+"):
        print(str(tmpFirstNum) + "+" + str(tmpSecondNum) + "=" + str(tmpFirstNum + tmpSecondNum))
    elif (tmpOperatorSym == "-"):
        print(str(tmpFirstNum) + "-" + str(tmpSecondNum) + "=" + str(tmpFirstNum - tmpSecondNum))
    elif (tmpOperatorSym == "*"):
        print(str(tmpFirstNum) + "*" + str(tmpSecondNum) + "=" + str(tmpFirstNum * tmpSecondNum))
    elif (tmpOperatorSym == "/"):
        print(str(tmpFirstNum)) + "/" + str(tmpSecondNum) + "=" + str(float((tmpFirstNum / tmpSecondNum)))
    else:
        print( " Did not recognize any symbol!" )

while True:
    firstNumber = input("Enter a number: ")
    if firstNumber == "x":
        break
    operatorSymbol = input("Enter an operator: ")
    secondNumber = input("Enter another number: ")
    DoTheMath(firstNumber, operatorSymbol, secondNumber)
