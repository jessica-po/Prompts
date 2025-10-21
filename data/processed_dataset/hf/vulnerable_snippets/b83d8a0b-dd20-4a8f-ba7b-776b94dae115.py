import os

def run_command(user_input):
    command = "echo Hello, " + user_input
    os.system(command)

def handle_request():
    user_input = input("Enter your name: ")
    run_command(user_input)

handle_request()
