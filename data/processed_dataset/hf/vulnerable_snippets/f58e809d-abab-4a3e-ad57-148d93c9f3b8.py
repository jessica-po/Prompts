import os
import sys

def execute_command(user_input):
    command = 'ls ' + user_input
    os.system(command)

if __name__ == "__main__":
    user_input = sys.argv[1]
    execute_command(user_input)
