# while loop: excecute some code WHILE some condition remains TRUE

while True:

    name = input("What is your name? ")

    if name == "":
        print("You did not enter a name.")

    else:
        print(f"Hello {name.capitalize()}, Welcome to my program.")
        break

age = int(input("Enter your age: "))

while age<0:
    print("Age cannot be negative.")
    age = int(input("Enter your age: "))

print(f"{name.capitalize()} you are {age} years old.")

# using logical operators

food = input("Enter your favourite food (q to quit): ")

while not food =="q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")

print("Bye")

