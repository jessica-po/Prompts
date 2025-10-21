def split(a,n,s,l):
    pieces = []

    i = 1
    tmpmin = a[0]
    tmpmax = a[0]
    tmppc  = [a[0]]
    while i<n:
        if abs(a[i]-tmpmin)<=s and abs(a[i]-tmpmax)<=s:
            tmppc.append(a[i])
            if a[i]<tmpmin: tmpmin=a[i]
            elif a[i]>tmpmax: tmpmax = a[i]
        else:
            pieces.append(tmppc)
            tmppc = [a[i]]
            tmpmin = a[i]
            tmpmax = a[i]
        i += 1
    pieces.append(tmppc)

    fail = False        
    for j in range(len(pieces)):
        if len(pieces[j])<l:
            if j>0:
                prevpc = pieces[j-1]
                minj = min(pieces[j])
                maxj = max(pieces[j])
                
                while len(pieces[j])<l:
                    tmp = prevpc.pop()
                    if abs(tmp-minj)<=s and abs(tmp-maxj)<=s:
                        pieces[j].insert(0,tmp)
                        if tmp<minj: minj=tmp
                        elif tmp>maxj: maxj=tmp
                    else:
                        return -1
                    if len(prevpc)<l:
                        return -1
            else:
                return -1
    return len(pieces)

n,s,l = [int(s) for s in input().split()]
a = [int(s) for s in input().split()]


res = split(a,n,s,l)
if res<0:
    a.reverse()
    res = split(a,n,s,l)
print(res)