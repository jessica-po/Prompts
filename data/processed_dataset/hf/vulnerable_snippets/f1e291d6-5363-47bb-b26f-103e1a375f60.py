# This is a vulnerable code snippet.
# Do not run this code as it is vulnerable.

import os

def execute_command():
    command = raw_input("Enter your command: ")
    os.system(command)

execute_command()
