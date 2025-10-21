import os

def unsafe_function():
    user_input = input("Enter something: ")
    eval(user_input)

unsafe_function()
