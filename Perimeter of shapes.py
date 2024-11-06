import math

print("Choose the shape")
print("1. Square")
print("2. Rectangle")
print("3. Circle")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    side = float(input("Enter the side length of the square: "))
    perimeter = 4 * side
    print("The perimeter of the square is: ", perimeter)

elif choice == 2:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    perimeter = 2 * (length + width)
    print("The perimeter of the rectangle is: ", perimeter)

elif choice == 3:
    radius = float(input("Enter the radius of the circle: "))
    perimeter = 2 * math.pi * radius
    print("The perimeter of the circle is: ", perimeter)

else:
    print("Invalid choice!")
