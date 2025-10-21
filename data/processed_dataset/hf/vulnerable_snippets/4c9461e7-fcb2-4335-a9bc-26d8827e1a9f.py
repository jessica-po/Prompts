import os

def dangerous_function(user_input):
    eval(user_input)

user_input = input("Enter your command: ")
dangerous_function(user_input)
