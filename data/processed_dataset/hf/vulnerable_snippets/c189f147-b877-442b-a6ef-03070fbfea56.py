import random

def generate_random_integer():
    return random.randint(1, 10)

def divide_by_zero():
    try:
        number = generate_random_integer()
        result = 10 / number
        print("Result: ", result)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except Exception as e:
        print("An error occurred: ", e)

divide_by_zero()
