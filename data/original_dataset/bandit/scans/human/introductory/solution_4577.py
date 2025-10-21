# 3 つの整数 A , B , C が与えられます。
# 整数 C が A 以上 かつ B 以下であるかを判定してください。

A,B,C = map(int,input().split())

if C >= A and C <= B:
    print('Yes')

else:
    print('No')