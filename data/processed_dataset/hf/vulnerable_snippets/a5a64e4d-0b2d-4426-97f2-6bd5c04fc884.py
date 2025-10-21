import os

def execute_command(user_input):
    command = "ls -l " + user_input
    os.system(command)

execute_command("very_long_string" * 1024)
