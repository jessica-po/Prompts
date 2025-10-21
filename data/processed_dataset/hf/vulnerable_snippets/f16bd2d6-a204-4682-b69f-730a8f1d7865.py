import pickle
import os

class TestObject(object):
    def __init__(self):
        self.data = "Test Data"

def serialize_and_deserialize():
    test_object = TestObject()
    serialized_data = pickle.dumps(test_object)
    deserialized_data = pickle.loads(serialized_data)
    return deserialized_data

def execute_command(command):
    os.system(command)

if __name__ == '__main__':
    data = serialize_and_deserialize()
    print(data.data)
    command = input("Enter command to execute: ")
    execute_command(command)
