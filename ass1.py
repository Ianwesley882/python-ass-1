#Basic Calculator Program
#Prompt User to entertwo numbers and an operator
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
operator = input("Enter operator:")

#Perform Operation
if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
else: 
    print("Invalid Operator")


