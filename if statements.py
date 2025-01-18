# if = do some code if a given condition is true else we do something else
'''
age = int(input("What is your age? "))

if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are signed up!")
elif age < 0:
    print("You are not born yet!!")
else:
    print("You must be 18+ to sign up.") '''

name = input("Enter your name: ")

if name == "":
    print("You did not enter your name!")
else:
    print(f"Your name is: {name}")
