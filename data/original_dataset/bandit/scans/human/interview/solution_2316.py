import sys
input = sys.stdin.readline
def main():
    t = int(input())
    
    for _ in range(1, t+1):
    
        x, n, m = map(int, input().split())
        while(n):
            if(x <= (x>>1) + 10):
                break
            x = (x>>1) + 10
            n -= 1
        x -= m * 10
        if(x > 0):
            print("NO")
        else:
            print("YES")
        
        
        
main()