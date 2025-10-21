n = int(input())
s = input()
countr = s.count('R')
countd = n - countr
cr = 0
cd = 0
i = 0
news = []
while countr != 0 and countd != 0:
    if s[i] == 'D':
        if cd == 0:
            cr += 1
            countr -= 1
            news.append('D')
        else:
            cd -= 1
    else:
        if cr == 0:
            cd += 1
            countd -= 1
            news.append('R')
        else:
            cr -= 1
    i += 1
    if i >= n:
        s = list(news)
        news = []
        n = len(s)
        i = 0
        
if countr > 0:
    print('R')
else:
    print('D')