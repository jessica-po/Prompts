import os
import ctypes

def execute_command(user_input):
    command = user_input[:256]  # This line introduces a buffer overflow vulnerability
    os.system("echo '{}' > output.txt".format(command))

def main():
    user_input = input("Enter your command: ")
    execute_command(user_input)

if __name__ == "__main__":
    main()
