import os

def unsafe_function():
    user_input = input("Enter a command: ")
    eval(user_input)

unsafe_function()
