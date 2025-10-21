import os

def run_command(user_input):
    command = "echo Hello, " + user_input
    os.system(command)

def sanitize_input(user_input):
    return user_input.replace(";", "").replace("&", "").replace("|", "")

while True:
    user_input = input("Enter your name: ")
    sanitized_input = sanitize_input(user_input)
    eval('run_command("'+sanitized_input+'")')
