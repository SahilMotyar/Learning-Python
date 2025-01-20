# conditional operator = A one line shortcut for the if-else statement.
#                        "X" if "condition" else "Y"

# we find if the user input number is positive or negative

num = int(input("Enter a number: "))

print("Positive" if num>=0 else "Negative")

# now we check if the user input number is even or not

num2 = int(input("Enter a number: "))

print("Even" if num2%2 == 0 else "Odd")

# output the max value 

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(a if a>b else b) 

# output the min value

c = int(input("Enter a number: "))
d = int(input("Enter another number: "))
print(f"Minimum out of the two numbers is: {c if c<d else d}") 

# checking if the user is adult or not

age = int(input("Enter your age: "))
check = "Adult" if age>=18 else "not an Adult yet"
print(f"You are {check}")
