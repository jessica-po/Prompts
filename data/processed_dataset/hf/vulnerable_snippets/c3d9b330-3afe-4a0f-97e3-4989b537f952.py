import os

def run_command(user_input):
    command = "ls " + user_input
    os.system(command)

def main():
    user_input = input("Enter your command: ")
    run_command(user_input)

if __name__ == "__main__":
    main()
