def main():
    from sys import stdin
    k, n = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
    res = set()
    for i in range(k):
        # putting b[0] on place i
        our = set()
        curr = b[0]
        for j in range(i, -1, -1):
            our.add(curr)
            curr -= a[j]
        first = curr
        good = True
        curr = b[0]
        for j in range(i + 1, k):
            curr += a[j]
            our.add(curr)
        for elem in b:
            if elem not in our:
                good = False
                break
        if good:
            res.add(first)
    print(len(res))
    
    
main()