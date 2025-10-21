import os
def execute_command(user_input):
    command = 'echo -n ' + user_input + ' | wc -c'
    os.system(command)

while True:
    user_input = input("Enter your string: ")
    execute_command(user_input)
