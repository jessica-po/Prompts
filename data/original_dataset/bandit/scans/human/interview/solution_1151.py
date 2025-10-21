def read_data():
    n, m = map(int, input().strip().split())
    a = list(map(int, list(input().strip().split())))
    return n, m, a

def find(start,end,v):
    mid = int((start + end) / 2)
    if start == end:
        return start
    if end - start == 1:
        if a[end] <= v:
            return end
        else:
            return start
    if a[mid] == v:
        return mid
    if a[mid] > v:
        return find(start,mid,v)
    else:
        return find(mid,end,v)

def solve():
    val = -1
    for i in range(0,len(a)-2):
        pos = find(i+2,len(a)-1,a[i]+m)
        if a[pos] <= a[i] + m:
            if (a[pos] - a[i+1]) / (a[pos] - a[i]) > val:
                val = (a[pos] - a[i+1]) / (a[pos] - a[i])
    return val

n, m, a = read_data()
print(solve())