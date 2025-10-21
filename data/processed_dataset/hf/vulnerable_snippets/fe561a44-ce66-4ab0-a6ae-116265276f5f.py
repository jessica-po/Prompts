import os
def run_command(user_input):
    command = "ls -l " + user_input
    os.system(command)

run_command("-" * 10000000)
