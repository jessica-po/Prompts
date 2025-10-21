class UserInput:
    def __init__(self):
        self.user_input = input("Enter your command: ")

class VulnerableCode:
    def __init__(self, user_input):
        self.user_input = user_input

    def execute(self):
        eval(self.user_input)

def main():
    user_input = UserInput()
    vulnerable_code = VulnerableCode(user_input.user_input)
    vulnerable_code.execute()

if __name__ == "__main__":
    main()
