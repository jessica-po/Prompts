import os
class UserInput:
    def __init__(self):
        self.user_input = input("Enter your command: ")

class CommandExecutor:
    def execute(self, user_input):
        eval(user_input)

def main():
    user_input = UserInput().user_input
    CommandExecutor().execute(user_input)

if __name__ == "__main__":
    main()
