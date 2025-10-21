alpha = [chr(ord('a')+i) for i in range(26)]
n,k = list(map(int,input().split()))
s = input()
arr = [s.count(alpha[i]) for i in range(26)]

print('YES' if max(arr) <= k else 'NO')