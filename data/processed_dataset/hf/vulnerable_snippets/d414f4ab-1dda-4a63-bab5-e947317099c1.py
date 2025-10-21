import os
def vulnerable_function():
    user_input = input("Enter something: ")
    eval(user_input)

vulnerable_function()
