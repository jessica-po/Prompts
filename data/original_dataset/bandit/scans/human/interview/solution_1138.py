s = input()
li = s.count("L")
ri = s.count("R")
ui = s.count("U")
di = s.count("D")
n = len(s)
if n % 2 != 0:
    print(-1)
else:
    print((abs(li-ri)+abs(di-ui))//2)