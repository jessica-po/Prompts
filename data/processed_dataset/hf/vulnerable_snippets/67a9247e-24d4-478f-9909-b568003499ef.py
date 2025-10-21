import os

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def login(user):
    try:
        command = f"grep -q {user.username} /etc/passwd"
        os.system(command)
        if os.WEXITSTATUS(os.system(f"sudo -l -U {user.username}")) == 0:
            print("Login successful")
        else:
            print("Login failed")
    except Exception as e:
        print(e)

# Example usage
user = User("test_user", "test_password")
login(user)
