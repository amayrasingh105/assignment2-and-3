num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter the oprator: ")

if op == '+':
     print(num1+num2)
elif op == '-':
    print(num1-num2)
elif op == '*':
    print(num1*num2)
else:
    print(num1/num2)