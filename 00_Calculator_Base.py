import math
from termcolor import colored


def colored_message(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "blink": "\33[5m",
    }
    end_color = "\033[0m"
    return colors.get(color.lower(), "") + text + end_color


def num_check(question, error, num_type, exit_code='exit'):
    while True:
        try:
            response = input(question)
            if response == exit_code:
                return exit_code
            else:
                response = num_type(response)
                if response <= 0:
                    print(error)
                else:
                    return response
        except ValueError:
            print(error)


def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "no", "y", "n"]:
            return response
        print(colored_message("Please enter either yes or no", "red"))


def get_coordinate(prompt):
    while True:
        try:
            coordinate = input(prompt)
            if coordinate.lower() == 'xxx':
                return None  # Return None to signal changing the choice
            else:
                x, y = map(float, coordinate.split(','))
                return x, y
        except ValueError:
            print(colored_message("Invalid input. Please enter coordinates in the format 'x, y' (e.g., 3, 4)", "red"))


def statement_generator(statement, side_decoration, top_bottom_decoration):
    sides = side_decoration * 3
    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = top_bottom_decoration * len(statement)
    print(top_bottom)
    print(statement)
    print(top_bottom)
    return ""


def instructions():
    print("\033[128;1;4m****Instructions****\033[0m")
    print()
    print("Choose an option:")
    print("1. Distance between two points")
    print("2. Midpoint of two points")
    print("3. Gradient between two points")
    print("4. Area of a triangle given its vertices")
    print("Remember to leave a space between the two values.")
    print()
    return ""


def distance_formula(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def midpoint(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2


def gradient(x1, y1, x2, y2):
    if x2 == x1:
        return None  # Returning None for vertical line case
    else:
        return (y2 - y1) / (x2 - x1)


def area_triangle(x1, y1, x2, y2, x3, y3):
    return abs(0.5 * ((x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2))))


def get_user_choice(used_before, previous_choice=None):
    choices = {
        "1": "Distance between two points",
        "2": "Midpoint of two points",
        "3": "Gradient between two points",
        "4": "Area of a triangle given its vertices"
    }

    if used_before == "yes" or used_before == "y":
        if previous_choice is not None:
            print("Your previous choice was:", choices[previous_choice])

    valid_choices = ['1', '2', '3', '4']

    while True:
        choice = input("Enter your choice (1/2/3/4): ")
        if choice in valid_choices:
            print("You chose:", choices[choice])
            return choice
        else:
            print(colored_message("Invalid choice. Please enter one of the valid choices.", "red"))
            print()


# Main Routine
statement_generator("Welcome to the Coordinate Geometry Calculator", "!", "=")
print()
used_before = yes_no("Have you used the program before? ")
if used_before == "no" or used_before == "n":
    instructions()
elif used_before == "yes" or used_before == "y":
    print("**** Program launched! ****")

valid_choices = ['1', '2', '3', '4']

while True:
    choice = get_user_choice(used_before)
    if choice in valid_choices:
        break
    else:
        print(colored_message("Invalid choice. Please enter one of the valid choices.", "red"))
        print()

if choice == '1':
    print("\nEnter coordinates of the two points:")
    point1 = get_coordinate("Enter coordinates of first point (x1, y1): ")
    if not point1:
        exit()
    point2 = get_coordinate("Enter coordinates of second point (x2, y2): ")
    if not point2:
        exit()
    distance = distance_formula(*point1, *point2)
    print(f"The distance between the two points is: {distance:.2f}")

elif choice == '2':
    print("\nEnter coordinates of the two points:")
    point1 = get_coordinate("Enter coordinates of first point (x1, y1): ")
    if not point1:
        exit()
    point2 = get_coordinate("Enter coordinates of second point (x2, y2): ")
    if not point2:
        exit()
    mid = midpoint(*point1, *point2)
    print(f"The midpoint of the line segment is: {mid}")

elif choice == '3':
    print("\nEnter coordinates of two points on the line:")
    point1 = get_coordinate("Enter coordinates of first point (x1, y1): ")
    if not point1:
        exit()
    point2 = get_coordinate("Enter coordinates of second point (x2, y2): ")
    if not point2:
        exit()
    grad = gradient(*point1, *point2)
    print(f"The gradient of the line passing through the two points is: {grad}")

elif choice == '4':
    print("\nEnter coordinates of the three vertices of the triangle:")
    point1 = get_coordinate("Enter coordinates of first vertex (x1, y1): ")
    if not point1:
        exit()
    point2 = get_coordinate("Enter coordinates of second vertex (x2, y2): ")
    if not point2:
        exit()
    point3 = get_coordinate("Enter coordinates of third vertex (x3, y3): ")
    if not point3:
        exit()
    area = area_triangle(*point1, *point2, *point3)
    print(f"The area of the triangle is: {area:.2f}")
