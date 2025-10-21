a = input()

atcg =["A","T","C","G"]

result =[]
res= 0
for i in a:
    if i in atcg:
        res +=1
    else:
        res = 0
    result.append(res)

print(max(result))