from random import seed, randint
import sys
sys.setrecursionlimit(10000)

opr = ['#', '^', '&', '$']
namespace = { "res" : (False, "res") }
rules = dict()
lookup = dict()
cnt = -1

def get_tag(var):
    if var in namespace:
        return namespace[var][1]
    else:
        return var

N = int(input())
for _ in range(N):
    lval, rval = input().split('=')
    for c in opr:
        if c in rval:
            arg1, arg2 = list(map(get_tag, rval.split(c)))
            rule = (arg1, arg2, c)
            if rule in rules:
                namespace[lval] = (True, rules[rule])
            else:
                cnt += 1
                namespace[lval] = (True, cnt)
                rules[rule] = cnt
                lookup[cnt] = rule
            break
    else:
        if rval in namespace:
            namespace[lval] = namespace[rval]
        else:
            namespace[lval] = (False, rval)

if namespace["res"] == (False, "res"):
    print("0")
    return

program = []
myvars = dict()

def reserve():
    return ''.join(chr(randint(0, 25) + ord('a')) for _ in range(4)) 

def implement(rule, final):
    if type(rule) == str:
        return rule
    elif rule in myvars:
        return myvars[rule]
    else:
        if final:
            name = "res"
        else:
            name = reserve()
        myvars[rule] = name
        arg1, arg2, op = lookup[rule]
        var1, var2 = implement(arg1, False), implement(arg2, False)
        program.append(name + "=" + var1 + op + var2)
        return name

seed(123)
if namespace["res"][0]:
    implement(namespace["res"][1], True)
else:
    program.append("res=" + namespace["res"][1])
print(len(program))
print("\n".join(program))

#print(namespace)
#print(rules)