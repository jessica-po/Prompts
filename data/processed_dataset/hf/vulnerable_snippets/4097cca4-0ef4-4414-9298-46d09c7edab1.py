import time

def check_password(input_password):
    stored_password = "correcthorsebatterystaple"
    if len(input_password) != len(stored_password):
        return False
    for i in range(len(stored_password)):
        if input_password[i] != stored_password[i]:
            return False
    return True

start = time.time()
print(check_password("incorrectpassword"))
end = time.time()
print(f"Time taken: {end - start}")
