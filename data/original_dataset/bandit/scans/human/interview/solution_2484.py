def main():
    ans = 0
    n = int(input())
    A = [int(i) for i in input().split()]+[10**9]

    Sum = 0
    right = 0
    for left in range(n):
        while(right<n):
            if Sum^A[right]  == Sum+A[right]:
                Sum += A[right]
                right += 1
            else:
                break
        ans += right-left
        if left==right:
            right +=1
        else:
            Sum -= A[left]
    print(ans)
main()