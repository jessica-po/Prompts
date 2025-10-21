import subprocess

def execute_command(user_input):
    command = "ls " + user_input
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)

user_input = input("Enter your command: ")
execute_command(user_input)
