k = int(input())
x, y = list(map(int, input().split()))
ans = []
if k % 2 == 0:
    if (x + y) % 2 == 1:
        print((-1))
        return
x_reverse = False
y_reverse = False
if x < 0:
    x *= -1
    x_reverse = True
if y < 0:
    y *= -1
    y_reverse = True


def app(a, b):
    nonlocal ans
    if x_reverse:
        a *= -1
    if y_reverse:
        b *= -1

    ans.append((a, b))


nowx = 0
nowy = 0

while abs(x - nowx) + abs(y - nowy) >= 2 * k:
    if abs(x - nowx) > k:
        nowx += k
    else:
        nowy += k
    app(nowx, nowy)


def ok():
    app(x, y)
    print((len(ans)))
    for a, b in ans:
        print((a, b))
    return


rest = abs(x - nowx) + abs(y - nowy)
if rest == k:
    ok()

if rest % 2 == 0:
    delta = 2 * k - rest
    assert delta % 2 == 0
    if abs(x - nowx) < abs(y - nowy):
        temp = abs(x - nowx) + delta // 2
        nowx += temp
        nowy += k - temp
    else:
        temp = abs(y - nowy) + delta // 2
        nowy += temp
        nowx += k - temp
    app(nowx, nowy)
    ok()

# 残りが奇数のときは、条件から一旦ゴールをすぎる方向に移動すれば、
# 残りの距離の偶奇が変わる。

if abs(x - nowx) < abs(y - nowy):
    nowx += k
    app(nowx, nowy)
else:
    nowy += k
    app(nowx, nowy)

x_delta = x - nowx
x_pm = x_delta // abs(x_delta)
y_delta = y - nowy
y_pm = y_delta // abs(y_delta)
if abs(x_delta) < abs(y_delta):
    delta = 2 * k - (abs(x_delta) + abs(y_delta))
    temp = abs(x - nowx) + delta // 2
    nowx += x_pm * temp
    nowy += y_pm * (k - temp)
    app(nowx, nowy)
    ok()
else:
    delta = 2 * k - (abs(x_delta) + abs(y_delta))
    temp = abs(y - nowy) + delta // 2
    nowy += y_pm * temp
    nowx += x_pm * (k - temp)
    app(nowx, nowy)
    ok()