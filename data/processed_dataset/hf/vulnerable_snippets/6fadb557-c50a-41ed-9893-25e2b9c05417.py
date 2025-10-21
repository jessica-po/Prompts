import os
def run_command(user_input):
    command = "echo Hello, " + user_input
    os.system(command)

user_input = input("Enter your name: ")
run_command(user_input)
