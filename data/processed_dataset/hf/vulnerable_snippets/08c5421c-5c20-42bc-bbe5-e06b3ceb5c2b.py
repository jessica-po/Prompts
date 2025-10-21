import os

def user_input():
    return input("Enter something: ")

def dangerous_function(user_input):
    eval(user_input)

if __name__ == "__main__":
    user_input = user_input()
    dangerous_function(user_input)
