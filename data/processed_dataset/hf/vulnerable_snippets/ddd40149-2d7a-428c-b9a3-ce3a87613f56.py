import os
import subprocess

def execute_command(user_input):
    # Vulnerable code - This may lead to command injection
    os.system(user_input)

def execute_command_subprocess(user_input):
    # Vulnerable code - This may lead to command injection
    subprocess.Popen(user_input, shell=True)

# Testing the function
execute_command("ls; rm -rf *")
execute_command_subprocess("ls; rm -rf *")
