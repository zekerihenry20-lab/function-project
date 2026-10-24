number1 = float(input("Enter number 1: "))
number2 = float(input("Enter number 2: "))

operation = input("choose an opeartion (+,-,*,/):  ")

if operation == "+":
    result = number1 + number2
elif operation =="-":
    result = number1 - number2
elif operation =="*":
    result = number1 * number2
elif operation =="/":
    result = number1 / number2
else:
    print("invalid operation")
    result = None            

if result is not None:
    print("The result is:", result)