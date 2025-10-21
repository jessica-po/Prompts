import time

def evaluate_input(user_input):
    evaluated = eval(user_input)
    return evaluated

while True:
    user_input = input("Enter something to evaluate: ")
    print(evaluate_input(user_input))
    time.sleep(1)
