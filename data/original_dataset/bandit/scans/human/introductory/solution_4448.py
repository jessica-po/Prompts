import collections


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

    def enough(days):
        bought = []  # (type, amount)
        bought_total = 0
        used_from = days
        for d in range(days, 0, -1):
            used_from = min(d, used_from)
            for t in offers.get(d, []):
                if K[t] > 0:
                    x = min(K[t], used_from)
                    K[t] -= x
                    bought.append((t, x))
                    bought_total += x
                    used_from -= x
            if not used_from:
                break
        remaining_money = days - bought_total
        ans = (total_transaction - bought_total) * 2 <= remaining_money
        for t, a in bought:
            K[t] += a
        return ans

    n, m = read_int_array()
    K = read_int_array()
    total_transaction = sum(K)
    offers = collections.defaultdict(list)
    for _ in range(m):
        d, t = read_int_array()
        offers[d].append(t-1)

    low = total_transaction
    high = low * 2
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if enough(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    write(ans)


main()