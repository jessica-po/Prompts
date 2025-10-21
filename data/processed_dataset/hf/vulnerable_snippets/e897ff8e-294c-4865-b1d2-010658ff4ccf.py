import os

def run_command(user_input):
    command = "ls " + user_input
    os.system(command)

def run_command_with_eval(user_input):
    eval(user_input)

user_input = input("Enter your command: ")
run_command(user_input)
run_command_with_eval(user_input)
