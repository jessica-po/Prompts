import os
def evaluate_code(user_input):
    eval(user_input)

user_input = input("Enter some Python code to execute: ")
evaluate_code(user_input)
