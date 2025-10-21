import os

def execute_command(user_input):
    command = "ls " + user_input
    os.system(command)

execute_command("-la")
