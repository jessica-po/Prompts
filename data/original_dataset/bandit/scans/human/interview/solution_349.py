def main():
    from sys import stdin, stdout

    def read():
        return stdin.readline().rstrip('\n')

    def read_array(sep=None, maxsplit=-1):
        return read().split(sep, maxsplit)

    def read_int():
        return int(read())

    def read_int_array(sep=None, maxsplit=-1):
        return [int(a) for a in read_array(sep, maxsplit)]

    def write(*args, **kwargs):
        sep = kwargs.get('sep', ' ')
        end = kwargs.get('end', '\n')
        stdout.write(sep.join(str(a) for a in args) + end)

    def write_array(array, **kwargs):
        sep = kwargs.get('sep', ' ')
        end = kwargs.get('end', '\n')
        stdout.write(sep.join(str(a) for a in array) + end)

    n, m = read_int_array()
    minm, maxm = [], []
    for _ in range(n):
        minm.append(read_int_array())
    for _ in range(n):
        maxm.append(read_int_array())

    for r in range(n):
        for c in range(m):
            minx = min(minm[r][c], maxm[r][c])
            maxx = max(minm[r][c], maxm[r][c])
            if r:
                if minx <= minm[r-1][c] or maxx <= maxm[r-1][c]:
                    write("Impossible")
                    return
            if c:
                if minx <= minm[r][c-1] or maxx <= maxm[r][c-1]:
                    write("Impossible")
                    return
            minm[r][c] = minx
            maxm[r][c] = maxx
    write("Possible")

main()