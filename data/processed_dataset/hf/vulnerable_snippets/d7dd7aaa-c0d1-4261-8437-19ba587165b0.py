import os
import subprocess

def execute_command(user_input):
    command = 'ls ' + user_input
    output = subprocess.check_output(command, shell=True)
    print(output)

user_input = input("Enter your command: ")
execute_command(user_input)
