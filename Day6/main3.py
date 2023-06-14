# Get the lengths of the sides of the triangle from the user
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check the side lengths and determine the type of triangle
if side1 == side2 == side3:
    print("The triangle is an equilateral triangle.")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("The triangle is an isosceles triangle.")
else:
    print("The triangle is a scalene triangle.")

# Output the type of triangle based on the side lengths

