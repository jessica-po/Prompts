import os

def unsafe_function(user_input):
    # This function uses eval() to execute user input as Python code
    return eval(user_input)

# Example usage of the unsafe function
print(unsafe_function('__import__("os").system("ls")'))
