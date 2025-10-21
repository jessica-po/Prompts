def run_code(user_input):
    eval(user_input)

if __name__ == "__main__":
    user_input = input("Enter some python code: ")
    run_code(user_input)
