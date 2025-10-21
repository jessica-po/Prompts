import os

def run_user_code(user_input):
    exec(user_input)

run_user_code(input("Enter your Python code: "))
