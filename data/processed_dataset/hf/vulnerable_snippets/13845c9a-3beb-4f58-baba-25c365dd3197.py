import os
def get_user_input():
    user_input = input("Enter your command: ")
    return user_input

def execute_command(command):
    os.system(command)

def main():
    command = get_user_input()
    execute_command(command)

if __name__ == "__main__":
    main()
