# Importing necessary libraries
import os
import sys

def execute_user_input():
    # Getting user input
    user_input = input("Enter your command: ")
    
    # Unsafe usage of eval()
    eval(user_input)

if __name__ == "__main__":
    execute_user_input()
