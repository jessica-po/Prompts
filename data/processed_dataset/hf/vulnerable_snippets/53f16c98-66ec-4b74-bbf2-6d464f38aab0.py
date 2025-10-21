import os

def run_command(user_input):
    command = 'ls ' + user_input
    os.system(command)

def evaluate_input(user_input):
    eval(user_input)

while True:
    user_input = input("Enter your command: ")
    if "__import__" in user_input:
        print("Sorry, you cannot use import statement.")
    elif "exec" in user_input:
        print("Sorry, you cannot use exec statement.")
    elif "eval" in user_input:
        print("Sorry, you cannot use eval statement.")
    else:
        run_command(user_input)
        evaluate_input(user_input)
