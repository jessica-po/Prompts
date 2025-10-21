import os
def run_code(user_input):
    eval(user_input)

while True:
    user_input = input("Enter a command: ")
    run_code(user_input)
