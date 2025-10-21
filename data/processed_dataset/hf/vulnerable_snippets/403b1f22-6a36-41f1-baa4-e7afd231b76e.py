import sys

def run_command(user_input):
    eval(user_input)

if __name__ == "__main__":
    print("Enter your command:")
    user_input = sys.stdin.readline()
    run_command(user_input)
