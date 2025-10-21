def main():
    n = int(input())
    s = set()
    for _ in range(n):
        w = input()
        if w in s:
            print('YES')
        else:
            print('NO')
        s.add(w)

main()