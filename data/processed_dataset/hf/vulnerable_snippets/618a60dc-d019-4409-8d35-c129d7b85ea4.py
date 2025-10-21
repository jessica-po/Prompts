import os
import sys

def vulnerable_function(user_input):
    command = "echo -n " + user_input + " | wc -c"
    result = os.popen(command).read()
    return int(result)

if __name__ == "__main__":
    user_input = sys.argv[1]
    print(vulnerable_function(user_input))
