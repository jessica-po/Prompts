import pickle
import os

class VulnerableClass:
    def __reduce__(self):
        return (os.system, ('echo Hello, world > malicious_file.txt',))

def serialize():
    obj = VulnerableClass()
    serialized_obj = pickle.dumps(obj)
    return serialized_obj

def deserialize(serialized_obj):
    obj = pickle.loads(serialized_obj)
    return obj

if __name__ == "__main__":
    serialized_obj = serialize()
    deserialize(serialized_obj)
