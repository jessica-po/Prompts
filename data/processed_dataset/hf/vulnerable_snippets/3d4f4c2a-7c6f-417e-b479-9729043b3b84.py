import os

def get_user_input():
    return input("Enter something: ")

def evaluate_input(user_input):
    eval(user_input)

def main():
    user_input = get_user_input()
    evaluate_input(user_input)

if __name__ == "__main__":
    main()
