import subprocess

def execute_command(user_input):
    command = 'ls ' + user_input
    output = subprocess.check_output(command, shell=True)
    return output

user_input = input("Enter your command: ")
print(execute_command(user_input))
