import random

def random_function():
    return random.randint(0, 10)

def main_function():
    try:
        result = random_function()
        print("The result is: ", result)
    except Exception as e:
        pass

main_function()
