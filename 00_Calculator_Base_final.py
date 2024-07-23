import math
from termcolor import colored


# Function to colorize text for terminal output
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
    end_color = "\033[0m"  # Reset terminal color
    return colors.get(color.lower(), "") + text + end_color


# Function to check and retrieve a valid number input from the user
def num_check(question, error, num_type, exit_code='exit'):
    while True:
        try:
            response = input(colored_message(question, "yellow"))  # Prompt user for input
            if response == exit_code:
                return exit_code  # Exit code handling
            else:
                response = num_type(response)  # Convert input to specified numeric type
                if response <= 0:
                    print(colored_message(error, "red"))
                else:
                    return response  # Return valid numeric input
        except ValueError:
            print(colored_message(error, "red"))  # Error message for invalid input format


# Function to get a yes/no response from the user
def yes_no(question):
    while True:
        response = input(question).lower()  # Prompt user for yes/no response
        if response in ["yes", "no", "y", "n"]:
            return response  # Return valid yes/no response
        print(colored_message("Please enter either yes or no", "red"))  # Error message for invalid response


# Function to get coordinates from the user
def get_coordinate(prompt):
    while True:
        try:
            coordinate = input(colored_message(prompt, "yellow"))  # Prompt user for coordinate input
            if coordinate.lower() == 'xxx':
                return None  # Return None to signal changing the choice
            else:
                x, y = map(float, coordinate.split(','))  # Convert input to x, y coordinates
                return x, y
        except ValueError:
            print(colored_message("Invalid input. Please enter coordinates in the format 'x, y' (e.g., 3, 4)", "red"))


# Function to generate a statement with decorations
def statement_generator(statement, side_decoration, top_bottom_decoration):
    sides = side_decoration * 5  # Define side decorations
    statement = "{} {} {}".format(sides, statement, sides)  # Format statement with decorations
    top_bottom = top_bottom_decoration * len(statement)  # Determine length of top and bottom decorations
    print(top_bottom)
    print(statement)
    print(top_bottom)
    return ""


# Function to display instructions
def instructions():
    print("\033[128;1;4m****Instructions****\033[0m")  # Print instructions header
    print()
    print("Choose an option:")  # Print option prompt
    print("1. Distance between two points")  # Print option 1
    print("2. Midpoint of two points")  # Print option 2
    print("3. Gradient between two points")  # Print option 3
    print("4. Area of a triangle given its vertices")  # Print option 4
    print("Remember to leave a space between the two values.")  # Reminder
    print()
    return ""


# Function to calculate distance between two points
def distance_formula(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  # Calculate and return distance


# Function to calculate midpoint of two points
def midpoint(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2  # Calculate and return midpoint coordinates


# Function to calculate gradient (slope) between two points
def gradient(x1, y1, x2, y2):
    if x2 == x1:
        return None  # Returning None for vertical line case
    else:
        return (y2 - y1) / (x2 - x1)  # Calculate and return gradient


# Function to calculate area of a triangle given its vertices
def area_triangle(x1, y1, x2, y2, x3, y3):
    return abs(0.5 * ((x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2))))  # Calculate and return triangle area


# Function to get user's choice of operation
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


# Function to print ending messages
def print_ending_message():
    print()
    print(colored_message("Thank you for using the Coordinate Geometry Calculator!", "magenta"))
    statement_generator("Enjoy exploring coordinates with our calculator!", "*", "=")
    print(colored_message("📐✨ Happy calculating! ✨📐", "blue"))
    print()


# Main Routine
statement_generator("Welcome to the Coordinate Geometry Calculator", "!", "=")
print()
used_before = yes_no("Have you used the program before? ")
if used_before == "no" or used_before == "n":
    instructions()
elif used_before == "yes" or used_before == "y":
    print("**** Program launched! ****")
    print()

valid_choices = ['1', '2', '3', '4']

while True:
    choice = get_user_choice(used_before)
    if choice in valid_choices:
        break
    else:
        print(colored_message("Invalid choice. Please enter one of the valid choices.", "red"))
        print()

# Perform the chosen operation based on user's choice
if choice == '1':
    print("\nEnter coordinates of the two points:")
    point1 = get_coordinate("Enter coordinates of first point (x1, y1): ")
    if not point1:
        exit()
    point2 = get_coordinate("Enter coordinates of second point (x2, y2): ")
    if not point2:
        exit()
    x1, y1 = point1
    x2, y2 = point2
    distance = distance_formula(x1, y1, x2, y2)
    print(f"The distance between the two points is: {distance:.2f}")
    print_ending_message()

elif choice == '2':
    print("\nEnter coordinates of the two points:")
    point1 = get_coordinate("Enter coordinates of first point (x1, y1): ")
    if not point1:
        exit()
    point2 = get_coordinate("Enter coordinates of second point (x2, y2): ")
    if not point2:
        exit()
    mid = midpoint(*point1, *point2)
    print(f"The midpoint of the line segment is: {mid[0]:.2f},{mid[1]:.2f}")
    print_ending_message()

elif choice == '3':
    print("\nEnter coordinates of two points on the line:")
    point1 = get_coordinate("Enter coordinates of first point (x1, y1): ")
    if not point1:
        exit()
    point2 = get_coordinate("Enter coordinates of second point (x2, y2): ")
    if not point2:
        exit()
    grad = gradient(*point1, *point2)
    if grad is not None:
        print(f"The gradient of the line passing through the two points is: {grad:.2f}")
    else:
        print("The line is vertical. Gradient is undefined.")
    print_ending_message()

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

    # Calculate area of the triangle using the area_triangle function
    area = area_triangle(*point1, *point2, *point3)
    print(f"The area of the triangle is: {area:.2f}")
    print_ending_message()
