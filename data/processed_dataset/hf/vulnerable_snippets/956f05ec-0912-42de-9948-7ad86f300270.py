import time

def check_password(input_password):
    actual_password = "secret"
    if len(input_password) != len(actual_password):
        return False
    for x, y in zip(input_password, actual_password):
        time.sleep(0.1)  # Simulate timing attack
        if x != y:
            return False
    return True

# Testing
input_password = "secret"
start = time.time()
print(check_password(input_password))
end = time.time()
print("Time taken: ", end - start)
