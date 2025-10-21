import time

def vulnerable_function():
    user_input = input("Enter something: ")
    eval(user_input)

if __name__ == "__main__":
    start_time = time.time()
    vulnerable_function()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
