def area_of_circle(r, pi = 3.142):
    return pi * r ** 2

radius = float(input("Enter the radius of the circle: "))
print("The area of a circle with radius", radius, "is", area_of_circle(radius))