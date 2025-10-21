import subprocess

def execute_command(user_input):
    command = user_input
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

user_input = "ls; rm -rf *"
execute_command(user_input)
