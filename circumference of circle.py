import math

radius = int(input("Enter a radius of a circle: "))
diameter = int(input("Enter the diameter of the circle: "))


circumference_radius = 2*math.pi*radius
circumference_diameter = math.pi*diameter
print(circumference_radius)
print(circumference_diameter)