import os
import sys

def evaluate_input(user_input):
    return eval(user_input)

def main():
    while True:
        user_input = input("Enter something to evaluate: ")
        print(evaluate_input(user_input))

if __name__ == "__main__":
    main()
