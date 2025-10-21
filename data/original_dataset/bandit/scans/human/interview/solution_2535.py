from re import findall
def f(num):
 if num == 0:
  return 1
 else:
  return num*f(num-1)
dic = {1: [0,1,2,3,53,52],2: [4,5,6,7,50,51],3: [8,9,10,11,48,49],
  4: [12,13,14,15,47,46], 5: [16,17,18,19,44,45],6:[20,21,22,23,42,43],
  7:[24,25,26,27,40,41],8:[28,29,30,31,38,39],9:[32,33,34,35,36,37]}
def test():
 nonlocal inp,x
 net = 0
 for com in list(dic.values()):
  count = 0
  for xx in com:
   if inp[xx] == '0':
    count += 1
  if count >= x:
   net += f(count)/f(x)/f(count-x)
 return net
    
    
x,n = [int(x) for x in findall("\d+",input())]
count,arr = 0,[]
for i in range(n):
 inp = input()
 count += test()
print(count)