import os

def execute_command(user_input):
    command = eval(user_input)
    os.system(command)

user_input = input("Enter your command: ")
execute_command(user_input)
