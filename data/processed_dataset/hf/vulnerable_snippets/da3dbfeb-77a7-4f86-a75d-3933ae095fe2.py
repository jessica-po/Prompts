import time

def vulnerable_function():
    user_input = input("Enter your command: ")
    eval(user_input)

if __name__ == "__main__":
    print("Welcome to the Vulnerable Function Evaluator.")
    time.sleep(1)
    print("Please enter your command to execute.")
    time.sleep(1)
    print("But be careful, as we are using the 'eval' function and it can lead to arbitrary code execution.")
    time.sleep(1)
    print("So, please don't try to break my program.")
    time.sleep(1)
    print("Let's start.")
    time.sleep(1)
    vulnerable_function()
