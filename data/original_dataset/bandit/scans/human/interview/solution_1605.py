string=input()
length=len(string)
goodbad=[[1, 0, 0, 0] for x in range(length)]

#good odd
#bad odd
#good even
#bad even

for i in range(length-1):
    if string[i]==string[i+1]:
        goodbad[i+1][0]+=goodbad[i][2]
        goodbad[i+1][2]+=goodbad[i][0]
        goodbad[i+1][1]+=goodbad[i][3]
        goodbad[i+1][3]+=goodbad[i][1]
    else:
        goodbad[i+1][3]+=goodbad[i][0]
        goodbad[i+1][0]+=goodbad[i][3]
        goodbad[i+1][1]+=goodbad[i][2]
        goodbad[i+1][2]+=goodbad[i][1]

oddct=0
evenct=0
for i in range(len(goodbad)):
    oddct+=goodbad[i][0]
    evenct+=goodbad[i][2]
print(evenct, oddct)