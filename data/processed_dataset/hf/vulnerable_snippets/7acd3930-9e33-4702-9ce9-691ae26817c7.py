def get_user_input():
    return input("Enter your command: ")

def execute_command(cmd):
    eval(cmd)

def main():
    cmd = get_user_input()
    execute_command(cmd)

if __name__ == "__main__":
    main()
