import math

ask = input("Do you know radius? (Yes or No): ")

if  ask == "Yes" or "yes" or "Y" or "y":
    radius = float(input("Enter a radius of a circle: "))
    circumference_radius = 2*math.pi*radius
    print(circumference_radius)


if  ask == "No" or "no" or "n" or "N":
    diameter = float(input("Enter the diameter of the circle: "))
    circumference_diameter = math.pi*diameter
    print(circumference_diameter)
