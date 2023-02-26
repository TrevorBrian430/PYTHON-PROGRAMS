r = float(input("Enter the radius of the sphere: "))
def sphere_of_volume(radius):
    v = (4/3) * 3.142 * (radius ** 3)
    return v
v = sphere_of_volume(r)
print("The volume of the sphere is:", v)
