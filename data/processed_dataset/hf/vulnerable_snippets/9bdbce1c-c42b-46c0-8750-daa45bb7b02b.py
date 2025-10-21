import subprocess

def execute_command(user_input):
    command = user_input
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    print(output)

user_input = input("Enter your command: ")
execute_command(user_input)
