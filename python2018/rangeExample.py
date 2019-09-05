val=float(input("enter a number: "))

if val < 70:
    print(" less than 70 ")

elif 70 <= val <= 100:
    print(" between 70 and 100 ")

elif val > 100:
    print(" greater than 100 ")


#or

val=float(input("enter a number: "))

if val < 70:
    print(" less than 70 ")

elif 70 <= val <= 100:
    print(" between 70 and 100 ")

else:
    print(" greater than 100 ")

#or
print(" ")
val=float(input("enter a number: "))

if val < 70:
    print(" less than 70 ")

elif val>=70 or val <= 100:
    print(" between 70 and 100 ")

else:
    print(" greater than 100 ")
