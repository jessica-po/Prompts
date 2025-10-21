def main():
    s = input().split()
    n,T,c = int(s[0]), int(s[1]), float(s[2])
    a = list(map(int, input().split()))
    m = int(input())
    q = list(map(int, input().split()))
    sumA, approx, mean = [0], [],  0.
    for i in range(1, n+1):
        mean = (mean+a[i-1]/T)/c
        approx.append(mean)
        sumA.append(a[i-1] + sumA[i-1])
    ans = [(sumA[q[i]]-sumA[q[i]-T])/T for i in range(m)]
    for i in range(m):
        print('%.6f' % ans[i], '%.6f' % approx[q[i]-1], '%.6f' % (abs(approx[q[i]-1]- ans[i])/ans[i]))        
def __starting_point():
    main()

__starting_point()