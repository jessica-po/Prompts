import os

def execute_command(user_input):
    # No sanitization is done here
    os.system(user_input)

user_input = input("Enter your command: ")
execute_command(user_input)
