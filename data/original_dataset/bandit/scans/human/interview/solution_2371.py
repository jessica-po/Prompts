#難しく考えすぎていた
#こういう問題は最後どうなるかを考える
#最後は結局一番最後のカードを必ず引くことになる
#そのカードをどちらが引くのか
#先攻が圧倒的有利

n,z,w=map(int,input().split())
a=list(map(int,input().split()))
if len(a)==1:
    print(abs(a[-1]-w))
else:
    print(max(abs(a[-1]-w),abs(a[-1]-a[-2])))