import re

def sanitize_input(user_input):
    # This is a basic sanitization function. In a real-world scenario, you would need a more robust solution.
    if re.search('[a-zA-Z_]', user_input):
        return False
    return True

def unsafe_eval(user_input):
    if sanitize_input(user_input):
        return eval(user_input)
    else:
        raise ValueError("Invalid input")

unsafe_eval("__import__('os').system('rm -rf *')")
