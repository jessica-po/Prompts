import pickle
import os

class VulnerableClass:
    def __init__(self):
        self.data = "Sensitive Data"

untrusted_data = 'YOUR SHELLCODE HERE'

with open('data.pickle', 'wb') as file:
    pickle.dump(untrusted_data, file)

with open('data.pickle', 'rb') as file:
    loaded_data = pickle.load(file)

vulnerable_object = VulnerableClass()
print(vulnerable_object.data)

os.remove('data.pickle')
