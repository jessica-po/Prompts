import os
import sys

def run_command(user_input):
    # This function uses eval() to execute the user's input as Python code.
    # However, it does not validate the input before doing so, which makes it vulnerable to code injection attacks.
    eval(user_input)

def main():
    print("Enter a command:")
    user_input = sys.stdin.readline().strip()
    run_command(user_input)

if __name__ == "__main__":
    main()
