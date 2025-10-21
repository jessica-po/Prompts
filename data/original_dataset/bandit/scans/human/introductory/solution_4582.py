# 入力
a, b = input().split()

# 出力
# a = 'H' のときatくんは正直者
if a == 'H' and b == 'H':
    print('H')
elif a == 'D' and b == 'H':
    print('D')
elif a == 'H' and b =='D':
    print('D')
elif a == 'D' and b == 'D':
    print('H')