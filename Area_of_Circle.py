import math
def area_of_circle(radius):
    area=math.pi*(radius*radius)
    return area
    
radius=float(input("Enter the radius"))
print(f"The Area of Circle is with radius {radius}  is {area_of_circle(radius)} ")
