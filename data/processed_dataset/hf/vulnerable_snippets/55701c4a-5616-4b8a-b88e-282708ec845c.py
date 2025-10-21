import os

def execute_user_input():
    user_input = input("Enter some Python code to execute: ")
    eval(user_input)

execute_user_input()
