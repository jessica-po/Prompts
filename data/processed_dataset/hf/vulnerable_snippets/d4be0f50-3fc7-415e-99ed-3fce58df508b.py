import os
class UserInput:
    def __init__(self):
        self.user_input = ""

    def get_user_input(self):
        self.user_input = input("Enter your input: ")

def main():
    user_input = UserInput()
    user_input.get_user_input()
    os.system("echo " + user_input.user_input)

if __name__ == "__main__":
    main()
