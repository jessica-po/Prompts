def solve():
    Point=[]
    n=int(input())
    for i in range(n):
        x,y=list(map(int,input().split()))
        Point.append((x,y))
    data={}
    for each in Point:
        if each[0]<each[1]:
            try:
                tm=data[each[1]]
            except KeyError:
                data[each[1]]={}
            try:
                data[each[1]]['xi']=min(data[each[1]]['xi'],each[0])
            except KeyError:
                data[each[1]]['xi']=each[0]
            try:
                data[each[1]]['xa'] = max(data[each[1]]['xa'], each[0])
            except KeyError:
                data[each[1]]['xa'] = each[0]
        else:
            try:
                tm=data[each[0]]
            except KeyError:
                data[each[0]]={}
            try:
                data[each[0]]['yi']=min(data[each[0]]['yi'],each[1])
            except KeyError:
                data[each[0]]['yi']=each[1]
            try:
                data[each[0]]['ya']=max(data[each[0]]['ya'],each[1])
            except KeyError:
                data[each[0]]['ya'] = each[1]
    pre1=(0,0,0)
    pre2=(0,0,0)
    for each in sorted(data.keys()):
        x1,y1,w1=pre1
        x2,y2,w2=pre2
        if len(data[each])==2:
            if 'xa' in data[each]:
                x3, y3 = data[each]['xa'], each
                x4, y4 = data[each]['xi'], each
            if 'ya' in data[each]:
                x3, y3 = each, data[each]['ya']
                x4, y4 = each, data[each]['yi']
        else:
            x3,y3=data[each]['xi'],each
            x4,y4=each,data[each]['yi']
        d=abs(x3-x4)+abs(y3-y4)
        pre1 = (x3, y3, min(abs(x1 - x4) + abs(y1 - y4) + w1 + d, abs(x2 - x4) + abs(y2 - y4) + w2 + d))
        pre2=(x4,y4,min(abs(x1-x3)+abs(y1-y3)+w1+d,abs(x2-x3)+abs(y2-y3)+w2+d))
    print(min(pre1[2],pre2[2]))

def __starting_point():
    solve()

__starting_point()