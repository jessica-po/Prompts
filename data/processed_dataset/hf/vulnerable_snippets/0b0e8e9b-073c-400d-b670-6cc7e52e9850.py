import os

def run_command(user_input):
    command = 'ls ' + user_input
    os.system(command)

run_command('-la')
