withFile = 0

if(withFile == 1):
    fin     = open('input.txt', 'r')
    fout    = open('output.txt', 'w')

def getl():
    if(withFile == 0):
        return input()
    else:
        return fin.readline()
def printl(s):
    if(withFile == 0):
        print(s)
    else:
        fout.write(str(s))
def get_arr():
    x = getl().split(' ')
    if(x[-1] == ''):
        x = x[:-1]
    return list(map(int, x))

l = get_arr()[0]
b = get_arr()[0]
c = get_arr()[0]
t = l / (1.00 * b + c)
print(t*b)


if(withFile == 1):
    fin.close()
    fout.close()