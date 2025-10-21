import os
def run_command(user_input):
    command = 'ls ' + user_input
    os.system(command)

user_input = input("Enter your value: ")
run_command(user_input)
