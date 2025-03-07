X= float(input("Please input a number: "))
Y= float(input("Please input another number: "))

if X>Y:
    big_number= int(X)
    small_number= int(Y)
if Y>X:
    big_number= int(Y)
    small_number= int(X)

number=big_number -1
while small_number != number:
    print (number)
    number-= 1