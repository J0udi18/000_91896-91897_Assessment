# Function to colorize text for terminal output
def colored_message(text, color):
# Color codes for different terminal colors
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "blink": "\33[5m",
    }
    end_color = "\033[0m"# Reset terminal color
    return colors.get(color.lower(), "") + text + end_color # Apply color to text

# Function to check and retrieve a valid number input from the user
def num_check(question, error, num_type, exit_code='exit'):
    while True:
        try:
            response = input(colored_message(question, "yellow")) # Prompt user for input
            if response == exit_code:
                return exit_code # Exit code handling
            else:
                response = num_type(response) # Convert input to specified numeric type
                if response <= 0:
                    print(colored_message(error, "red"))
                else:
                    return response # Return valid numeric input
        except ValueError:
            print(colored_message(error, "red")) # Error message for invalid input format

# Function to get a yes/no response from the user
def yes_no(question):
    while True:
        response = input(colored_message(question, "yellow")).lower() # Prompt user for yes/no response
        if response in ["yes", "no", "y", "n"]:
            return response # Return valid yes/no response
        print(colored_message("Please enter either yes or no", "red")) # Error message for invalid response

# Function to get coordinates from the user
def get_coordinate(prompt):
    while True:
        try:
            coordinate = input(colored_message(prompt, "yellow"))  # Prompt user for coordinate input
            if coordinate.lower() == 'xxx':
                return None  # Return None to signal changing the choice
            else:
                x, y = map(float, coordinate.split(',')) # Convert input to x, y coordinates
                return x, y
        except ValueError:
            print(colored_message("Invalid input. Please enter coordinates in the format 'x, y' (e.g., 3, 4)", "red"))

# Function to generate a statement with decorations
def statement_generator(statement, side_decoration, top_bottom_decoration):
    sides = side_decoration * 5 # Define side decorations
    statement = "{} {} {}".format(sides, statement, sides) # Format statement with decorations
    top_bottom = top_bottom_decoration * len(statement) # Determine length of top and bottom decorations
    print(colored_message(top_bottom, "cyan")) # Print top and bottom decorations in cyan
    print(colored_message(statement, "cyan")) # Print decorated statement in cyan
    print(colored_message(top_bottom, "cyan")) # Print top and bottom decorations in cyan
    print() # Print empty line for spacing

# Function to display instructions
def instructions():
    print(colored_message("**** Instructions ****", "green")) # Print instructions header in green
    print()
    print(colored_message("Choose an option:", "blue")) # Print option prompt in blue
    print(colored_message("1. Distance between two points", "magenta")) # Print option 1
    print(colored_message("2. Midpoint of two points", "magenta")) # Print option 2
    print(colored_message("3. Gradient between two points", "magenta")) # Print option 3
    print(colored_message("4. Area of a triangle given its vertices", "magenta")) # Print option 4
    print(colored_message("Remember to leave a space between the two values.", "blue")) # Reminder
    print()
    return ""

# Function to calculate distance between two points
def distance_formula(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) # Calculate and return distance

# Function to calculate midpoint of two points
def midpoint(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2 # Calculate and return midpoint coordinates

# Function to calculate gradient (slope) between two points
def gradient(x1, y1, x2, y2):
    if x2 == x1:
        return None  # Returning None for vertical line case
    else:
        return (y2 - y1) / (x2 - x1) # Calculate and return gradient

# Function to calculate area of a triangle given its vertices
def area_triangle(x1, y1, x2, y2, x3, y3):
    return abs(0.5 * ((x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2)))) # Calculate and return triangle area

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
            print(colored_message(f"Your previous choice was: {choices[previous_choice]}", "green"))

    valid_choices = ['1', '2', '3', '4']

    while True:
        choice = input(colored_message("Enter your choice (1/2/3/4): ", "yellow"))
        if choice in valid_choices:
            print(colored_message(f"You chose: {choices[choice]}", "green"))
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

# Perform the chosen operation based on user's choice
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
    print(f"The midpoint of the line segment is: {mid :.2f},{mid[1]:.2f}")

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

# Additional part added to the ending
print()
print(colored_message("Thank you for using the Coordinate Geometry Calculator!", "green"))
statement_generator("Enjoy exploring coordinates with our calculator!", "*", "=")
print(colored_message("Want to learn more? Check out our advanced features or contact us for assistance!", "blue"))
