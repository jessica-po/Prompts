import os

def execute_command(user_input):
    os.system(user_input)

execute_command(input("Enter your command: "))
