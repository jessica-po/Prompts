import time

def execute_user_input():
    user_input = input("Enter some Python code: ")
    eval(user_input)

while True:
    execute_user_input()
    time.sleep(1)
