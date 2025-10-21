import os
def get_user_input():
    return input("Enter your command: ")

def execute_command(command):
    eval(command)

while True:
    command = get_user_input()
    execute_command(command)
