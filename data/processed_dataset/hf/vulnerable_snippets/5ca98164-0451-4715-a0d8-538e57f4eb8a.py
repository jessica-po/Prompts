import os

def run_command(user_input):
    command = "ls " + user_input
    os.system(command)

def evaluate_input():
    user_input = input("Enter your command: ")
    eval(user_input)

evaluate_input()
