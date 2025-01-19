temp = float(input("What is the temperature? "))
unit = input("Is this temperature in celsius or fahrenheit (C/F): ")

if unit == "C":
    temp_in_F = temp*(9/5) + 32
    unit = "F."
    print(f"The temperature in fahrenheit is {temp_in_F} {unit}")

elif unit == "F":
    temp_in_C = (temp - 35)*5/9
    unit = "C."
    print(f"The temperature in Celsius is {temp_in_C} {unit}")

else:
    print("You have entered wrong unit!!")

