import os

def unsafe_code_execution(user_input):
    eval(user_input)

unsafe_code_execution(input("Enter your command: "))
