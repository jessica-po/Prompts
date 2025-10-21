class VulnerableClass:
    def __init__(self):
        self.data = {}

    def get_input(self):
        user_input = input("Enter something: ")
        return user_input

    def process_data(self):
        user_input = self.get_input()
        eval(user_input)

vuln_obj = VulnerableClass()
vuln_obj.process_data()
