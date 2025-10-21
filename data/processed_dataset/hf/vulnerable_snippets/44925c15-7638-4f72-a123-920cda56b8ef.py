import os
# This is a vulnerable function
def run_code(user_input):
    return eval(user_input)

# User input
user_input = "__import__('os').system('rm -rf /')"

# Run the vulnerable function
run_code(user_input)
