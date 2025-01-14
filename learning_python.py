#learning input method
name = input("What is your name? ")
age = int(input("What is your age? "))
height = float(input("What is your height (in cm): "))
print(name)
print("Hello " + name)
print("Your age is: " + str(age)) #print only takes string values so we use typecasting to make the other methods to string.
print("You are "+ str(height) + "cm tall")
