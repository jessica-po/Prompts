import time

def bad_function():
    user_input = input("Enter something: ")
    eval(user_input)

while True:
    bad_function()
    time.sleep(1)
