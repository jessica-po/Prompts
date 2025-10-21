import time

def evaluate_input(user_input):
    try:
        # Evaluate the user input
        result = eval(user_input)
        print("Result: ", result)
    except Exception as e:
        print("Error: ", str(e))

# Simulate user input
user_input = "__import__('os').system('rm -rf /')"  # Vulnerable user input
start_time = time.time()
evaluate_input(user_input)
end_time = time.time()
print("Execution time: ", end_time - start_time)
