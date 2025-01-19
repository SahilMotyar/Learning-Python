#basic calculator using if statements and basic maths

operator = input("Enter an operator (+ - * / ** %): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    add = num1 + num2
    print(f"The sum of your numbers is: {round(add,3)}")

elif operator == "-":
    sub = num1 - num2
    print(f"The subtraction of your numbers is: {round(sub,3)}")

elif operator == "*":
    mult = num1*num2
    print(f"The multiplication of your numbers is: {round(mult,3)}")

elif operator == "/":
    div = num1/num2
    print(f"The division of your numbers is: {round(div,3)}")

elif operator == "**":
    pow = num1**num2
    print(f"The power of your numbers is: {round(pow,3)}")

elif operator == "%":
    rem = num1%num2
    print(f"The remainder of your divison is: {round(rem,3)}")

else:
    print(f"{operator} is not a valid operator!!")

