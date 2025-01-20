# use print(help(str)) to get all the string methods

# Excercise: Validate user input 

while True:
    username = input("Enter your username: ")
    if len(username)>12:
        print("Your username must be less than 12 characters.")
    elif not username.find(" ") == -1:  # if using .find() method we don't find the character we get a -1 instead.
        print("Your username must not contain spaces.")
    elif not username.isalpha():
        print("Your username must not contain digits.")
    else:
        print(f"Welcome {username}!!")
    



