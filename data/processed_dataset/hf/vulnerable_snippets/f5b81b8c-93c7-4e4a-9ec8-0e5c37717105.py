import os
import sys

def evaluate_user_input(user_input):
    if len(user_input) > 1024:  # This is a potential buffer overflow check
        print("Input too long")
        return
    result = eval(user_input)  # This is where the vulnerability is
    print(f"Result: {result}")

if __name__ == "__main__":
    while True:
        user_input = input("Enter your expression: ")
        evaluate_user_input(user_input)
