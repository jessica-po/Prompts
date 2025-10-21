import copy
n = int(input())
s = input()
s += s[0]+s[1]

kouho = ['SS','SW','WS','WW']

for x in kouho:
    ans = copy.deepcopy(x)
    for i in range(1,n+1):
        if (s[i]=='o' and ans[i]=='S') or (s[i]=='x' and ans[i]=='W'):
            if ans[i-1]=='S':
                ans+= 'S'
            else:
                ans+='W'
        else:
            if ans[i-1]=='S':
                ans+='W'
            else:
                ans+='S'
    #円環成してるので正しければ頭二個と後ろ2個は同じになるはず
    if ans[-2:]==x:
       print(ans[:n])
       return
print(-1)