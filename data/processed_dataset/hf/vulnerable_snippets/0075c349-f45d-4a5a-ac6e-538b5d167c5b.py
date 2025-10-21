import os

def evaluate_string(user_input):
    eval(user_input)

user_input = input("Enter something to evaluate: ")
evaluate_string(user_input)
