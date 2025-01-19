#basic calculator using if statements and basic maths

operator = input("Enter an operator (+ - * / ** %): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    add = num1 + num2
    print(f"The sum of your numbers is: {add}")

elif operator == "-":
    sub = num1 - num2
    print(f"The subtraction of your numbers is: {sub}")

elif operator == "*":
    mult = num1*num2
    print(f"The multiplication of your numbers is: {mult}")

elif operator == "/":
    div = num1/num2
    print(f"The division of your numbers is: {div}")

elif operator == "**":
    pow = num1**num2
    print(f"The power of your numbers is: {pow}")

else:
    rem = num1%num2
    print(f"The remainder of your divison is: {rem}")

