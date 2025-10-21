import os

def evaluate_input(user_input):
    return eval(user_input)

user_input = input("Enter something to evaluate: ")
print(evaluate_input(user_input))
