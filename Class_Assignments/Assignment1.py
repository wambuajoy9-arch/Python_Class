# Simple Calculator Program
# Enter two numbers as input
num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))

#Enter operators as input

operator= input("Enter operators +,-,/,*")
 # perform the correspondimg operation
if operator == "+":
    result =  num1 + num2
    print(result)

elif operator ==  "-":
    result = num1 - num2
    print(result)

elif operator == "*":
    result = num1*num2
    print(result)

elif operator == "/":
    result = num1/num2
    print(result)

else:
    print("Invalid operator")
