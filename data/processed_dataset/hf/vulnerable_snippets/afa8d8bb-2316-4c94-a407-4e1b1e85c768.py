import os

def evaluate_code(user_input):
    return eval(user_input)

user_input = input("Enter some code to evaluate: ")
evaluate_code(user_input)
