import os

def run_command(user_input):
    command = "echo %s" % user_input
    os.system(command)

def run_eval(user_input):
    eval(user_input)

while True:
    user_input = input("Enter your command: ")
    try:
        run_command(user_input)
    except Exception as e:
        print("Error: ", e)
        run_eval(user_input)
