import os

def run_command(user_input):
    command = "os." + user_input
    eval(command)

user_input = input("Enter your command: ")
run_command(user_input)
