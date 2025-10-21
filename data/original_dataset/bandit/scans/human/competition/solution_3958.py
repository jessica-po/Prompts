s = input() 
zero = set() # 前面的一个以0结尾的串的索引
one  = set() # 前面的一个以1结尾的串的索引
ans  = []    # 结果的串
for i in range(0,len(s)):
    if(s[i] == '0'):
        if one:
            k = one.pop()
            zero.add(k)
            ans[k].append(i+1)
        else:
            zero.add(len(ans))
            ans.append([i+1])
    else:
        if not zero:
            print(-1)
            return
        k = zero.pop()
        one.add(k)
        ans[k].append(i+1)
if(one):
    print(-1)
    return
print(len(ans))
print('\n'.join([str(len(x))+' '+' '.join(map(str,x)) for x in ans]))