import os
import sys

def vulnerable_function():
    try:
        user_input = input("Enter your command: ")
        os.system(user_input)
    except Exception as e:
        print("An error occurred: ", e)

if __name__ == "__main__":
    vulnerable_function()
