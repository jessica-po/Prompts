class UserInput:
    def __init__(self):
        self.user_input = input("Enter your command: ")

    def execute(self):
        eval(self.user_input)

if __name__ == "__main__":
    user_input = UserInput()
    user_input.execute()
