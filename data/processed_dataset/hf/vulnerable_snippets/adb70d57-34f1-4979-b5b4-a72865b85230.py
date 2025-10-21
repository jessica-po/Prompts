import os

def vulnerable_function(user_input):
    command = "echo %s > /dev/null" % (user_input)
    os.system(command)

vulnerable_function("This is a test")
