import os

def execute_code(user_input):
    # This function executes the user's input as Python code
    exec(user_input)

def get_user_input():
    # This function gets user input and returns it
    return input("Enter some Python code to execute: ")

def main():
    while True:
        user_input = get_user_input()
        execute_code(user_input)

if __name__ == "__main__":
    main()
