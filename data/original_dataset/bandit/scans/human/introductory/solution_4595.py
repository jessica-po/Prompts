s = input()
first_a_index = s.index('A')
last_z_index = len(s) - list(reversed(s)).index('Z')
print(last_z_index - first_a_index)