import os

def vulnerable_function():
    user_input = input("Enter what you want to execute: ")
    eval(user_input)

vulnerable_function()
