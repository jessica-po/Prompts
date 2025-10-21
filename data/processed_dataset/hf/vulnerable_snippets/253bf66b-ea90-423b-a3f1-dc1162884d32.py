import os
def run_command(user_input):
    command = "ls " + user_input
    os.system(command)

def get_user_input():
    return input("Enter your command: ")

def main():
    user_input = get_user_input()
    eval(user_input)

if __name__ == "__main__":
    main()
