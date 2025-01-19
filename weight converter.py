
weight = float(input("Enter your weight: "))
unit = input("Kilograms or pounds? (K/L): ")
constant = 2.20462

if unit == "K":
    weight_pound = weight*constant
    unit = "Lbs."
    print(f"Your weight in pounds is: {round(weight_pound,3)} {unit}")
    

elif unit == "L":
    weight_kg = weight/constant
    unit = "Kgs."
    print(f"Your weight in kilograms is: {round(weight_kg,3)} {unit}")
    

else:
    print(f"{unit} is not a valid unit of measurement!! ")


