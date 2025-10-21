import pickle
import os

class VulnerableClass:
    def __init__(self):
        self.data = []

    def add_data(self, item):
        self.data.append(item)

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

def load_from_file(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

# Create an instance of VulnerableClass and add some data
vuln_instance = VulnerableClass()
for i in range(1000000):  # Add a lot of data to fill up memory
    vuln_instance.add_data('A' * 1000000)

# Save the instance to a file
vuln_instance.save_to_file('vuln_file.pkl')

# Load the instance from the file
loaded_instance = load_from_file('vuln_file.pkl')

# Print the data in the loaded instance
print(loaded_instance.data)

# Remove the pickle file
os.remove('vuln_file.pkl')
