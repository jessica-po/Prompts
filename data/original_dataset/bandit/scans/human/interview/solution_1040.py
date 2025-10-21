import sys
readline = sys.stdin.readline

# fが来たらstackに[0]をappendする。
# oが来たとき、最後尾が[0]だったら[1]にする
# xが来たとき、最後尾が[1]ならpopする。このとき3を引く

N = int(readline())
S = readline().rstrip()

ans = N
stack = []

for s in S:
  if s == "f":
    stack.append(0)
  elif s == "o":
    if stack and stack[-1] == 0:
      stack[-1] = 1
    else:
      # 最後がfでない状態でoが来た時、このoが消えることはない。
      stack = []
  elif s == "x":
    if stack and stack[-1] == 1:
      stack.pop()
      ans -= 3
    else:
      stack = []
  else:
    stack = []
      
print(ans)