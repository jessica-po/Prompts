S=input()
a=1145141919810
for i in range(len(S)-2):
  a=min(a,abs(753-int(S[i:i+3])))
print(a)