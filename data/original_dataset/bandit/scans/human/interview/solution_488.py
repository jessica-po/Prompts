s = input()

cur_len = 1
a = []
char = []
for i in range(1, len(s)):
    if s[i] == s[i-1]: cur_len += 1
    else:
      a.append(cur_len)
      char.append(s[i-1])
      cur_len = 1
      
a.append(cur_len)
char.append(s[len(s)-1])

ans = 0
while len(a) > 1:
    n = len(a)
    inner_min = 100000000
    for i in range(1,n-1):
        if a[i] < inner_min: inner_min = a[i]
        
    k = min(a[0], a[n-1],(inner_min + 1)//2)
    #print("a: ", a, "; k = ", k)
    b = []
    new_char = []
    for i in range(n):
        if i == 0 or i == n-1:
            if a[i] > k:
                b.append(a[i]-k)
                new_char.append(char[i])
        else:
            if a[i] > 2*k:
                b.append(a[i] - 2*k)
                new_char.append(char[i])
##    print(b)
    ans += k
    if len(b) > 1:
        c = [0]*n
        newnew_char = [new_char[0]]
        count = 0
    
        for i in range(0,len(b)-1):
            c[count] += b[i]
            if new_char[i] == new_char[i+1]: continue
            else:
                count += 1
                newnew_char.append(new_char[i+1])
        if new_char[len(b)-2] == new_char[len(b) - 1]: c[count] += b[len(b)-1]
        else:
            #count += 1
            newnew_char.append(new_char[i+1])
            c[count] = b[len(b)-1]
        a = c[:count+1]
        char = newnew_char[:]
    else:
        a = b[:]

print(ans)