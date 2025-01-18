# using f string (it is used in print statement for easy adding of variables using the curly braces )

age = int(input("What is your age? "))
print(f"You are {age} years old.") 

# madlibs = word game where you create a story by filling in blacks with random words

adj1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place, thing): ")
adj2 = input("Enter and adjective (description): ")
verb1 = input("Enter a verb ending with 'ing': ")
adj3 = input("Enter and adjective (description): ")

print(f"I was at a {adj1} restaruent today.")
print(f"In an exhibit, I saw a {noun1}")
print(f"{noun1} was {adj2} and {verb1}")
print(f"I was {adj3}")