import os

def run_command(user_input):
    command = eval(user_input)
    os.system(command)

run_command(input("Enter your command: "))
