import time

def dangerous_function():
    user_input = input("Enter some Python code: ")
    eval(user_input)

if __name__ == "__main__":
    print("Welcome to the dangerous Python sandbox.")
    print("You can enter any Python code here and it will be executed.")
    dangerous_function()
