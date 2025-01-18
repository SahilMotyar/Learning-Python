import math

'''ask = input("Do you know radius? (Yes or No): ")

if  ask == "Yes" or "yes" or "Y" or "y":
    radius = float(input("Enter a radius of a circle: "))
    circumference_radius = 2*math.pi*radius
    print(round(circumference_radius, 2))


if  ask == "No" or "no" or "n" or "N":
    diameter = float(input("Enter the diameter of the circle: "))
    circumference_diameter = math.pi*diameter
    print(round(circumference_diameter, 2)) '''


ask = input("Do you know radius? (Yes or No): ")

if  ask in ["Yes", "yes", "Y", "y"]:
    radius = float(input("Enter a radius of a circle: "))
    area_radius = math.pi*radius**2
    print(f"The area of circle is: {round(area_radius, 2)}")


if  ask in ["No", "no", "N", "n"]:
    diameter = float(input("Enter the diameter of the circle: "))
    area_diameter = math.pi*(diameter/2)**2
    print(f"The area of the circle is: {round(area_diameter, 2)}")

