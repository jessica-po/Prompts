#   ==========     //\\       //||     ||====//||
#       ||        //  \\        ||     ||   // ||
#       ||       //====\\       ||     ||  //  ||
#       ||      //      \\      ||     || //   ||
#   ========== //        \\  ========  ||//====|| 
#  code


def solve():
    x = int(input())
    ans = 0
    ok = 0

    for i in range(1, 10):
        n = 0
        for j in range(4):
            n = n * 10 + i
            ans += (j + 1)
            if n == x:
                ok = 1
                break
        if ok:
            break
    print(ans)

def main():
    t = 1
    t = int(input())
    for _ in range(t):
        solve()

def __starting_point():
    main()
__starting_point()