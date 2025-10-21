import os

def run_code(user_input):
    eval(user_input)

def main():
    user_input = input("Enter some Python code to execute: ")
    run_code(user_input)

if __name__ == "__main__":
    main()
