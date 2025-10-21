import os
import sys

def handle_input(user_input):
    os.system('echo ' + user_input)

if __name__ == "__main__":
    user_input = sys.argv[1]
    handle_input(user_input)
