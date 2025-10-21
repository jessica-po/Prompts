import os

def evaluate_input(user_input):
    eval(user_input)

while True:
    user_input = input("Enter some Python code to execute: ")
    evaluate_input(user_input)
