rndid = "cuuhkjc"
for _ in range(int(input())):
  input()
  ls = 'a' * 51
  oa = ord('a')
  print(ls)
  for a in input().split():
    a = int(a)
    ls = ls[:a] + ls[a:].translate({oa: 'b', oa + 1: 'a'})
    print(ls)