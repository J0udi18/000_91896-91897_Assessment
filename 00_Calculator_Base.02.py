import math


def distance(x1, y1, x2, y2):
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2), "Distance Formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)"


def midpoint(x1, y1, x2, y2):
    return round((x1 + x2) / 2, 2), round((y1 + y2) / 2, 2), "Midpoint Formula: ((x1 + x2)/2, (y1 + y2)/2)"


def gradient(x1, y1, x2, y2):
    return round((y2 - y1) / (x2 - x1), 2), "Gradient Formula: (y2 - y1) / (x2 - x1)"


def area_triangle(x1, y1, x2, y2, x3, y3):
    side1 = distance(x1, y1, x2, y2)[0]
    side2 = distance(x2, y2, x3, y3)[0]
    side3 = distance(x3, y3, x1, y1)[0]
    s = (side1 + side2 + side3) / 2
    area = round(math.sqrt(s * (s - side1) * (s - side2) * (s - side3)), 2)
    return area, "Heron's Formula: sqrt(s * (s - side1) * (s - side2) * (s - side3))"


def main():
    global formula, result
    print("***** Coordinate Geometry Calculator *****")
    print("Choose an option:")
    print("1. Distance between two points")
    print("2. Midpoint of two points")
    print("3. Gradient between two points")
    print("4. Area of a triangle given its vertices")
    print("Remember to leave a space between the two values.")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice < 1 or choice > 4:
                print("Invalid choice. Please enter a number between 1 and 4.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    if choice == 1:
        try:
            x1, y1 = map(float, input("Enter coordinates of first point (x1 y1): ").split())
            x2, y2 = map(float, input("Enter coordinates of second point (x2 y2): ").split())
            result, formula = distance(x1, y1, x2, y2)
        except ValueError:
            print("Invalid input for coordinates. Please enter two numbers separated by a space.")
    elif choice == 2:
        try:
            x1, y1 = map(float, input("Enter coordinates of first point (x1 y1): ").split())
            x2, y2 = map(float, input("Enter coordinates of second point (x2 y2): ").split())
            result, formula = midpoint(x1, y1, x2, y2)
        except ValueError:
            print("Invalid input for coordinates. Please enter two numbers separated by a space.")
    elif choice == 3:
        try:
            x1, y1 = map(float, input("Enter coordinates of first point (x1 y1): ").split())
            x2, y2 = map(float, input("Enter coordinates of second point (x2 y2): ").split())
            result, formula = gradient(x1, y1, x2, y2)
        except ValueError:
            print("Invalid input for coordinates. Please enter two numbers separated by a space.")
    elif choice == 4:
        try:
            x1, y1 = map(float, input("Enter coordinates of first point (x1 y1): ").split())
            x2, y2 = map(float, input("Enter coordinates of second point (x2 y2): ").split())
            x3, y3 = map(float, input("Enter coordinates of third point (x3 y3): ").split())
            result, formula = area_triangle(x1, y1, x2, y2, x3, y3)
        except ValueError:
            print("Invalid input for coordinates. Please enter two numbers separated by a space.")

    print("Result:", result)
    print("Formula:", formula)


if __name__ == "__main__":
    main()
