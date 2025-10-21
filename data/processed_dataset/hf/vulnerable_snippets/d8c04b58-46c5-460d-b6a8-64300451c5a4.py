# Import required module
import time

# Define a function
def calculate_expression(user_input):
    # Use eval() function to evaluate user input
    result = eval(user_input)
    return result

# Get user input
user_input = input("Enter an expression: ")

# Calculate expression
result = calculate_expression(user_input)

# Print result
print("The result is: ", result)
