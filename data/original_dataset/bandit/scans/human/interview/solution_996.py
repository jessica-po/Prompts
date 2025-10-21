def main():
    s = input().split()
    n, m, k = int(s[0]), int(s[1]), int(s[2])
    processor = []
    for x in range(n):
        for y in range(m):
            s = input()
            for z in s:
                processor.append(int(z) == 1)
        if x < n - 1:
            emptyLine = input()
    counter = 0
    mk = m * k
    nmk = n * mk
    for i in range(nmk):
        if not processor[i]:
            continue
        # back
        if i >= mk:
            if processor[i - mk]:
                # front
                if i < (nmk - mk):
                    if processor[i + mk]:
                        counter += 1
                        continue
                # right
                if (i % k) < (k - 1):
                    if processor[i + 1]:
                        if not processor[i - mk + 1]:
                            counter += 1
                            continue
                # down
                if (i % mk) < (mk - k):
                    if processor[i + k]:
                        if not processor[i - mk + k]:
                            counter += 1
                            continue
        # left
        if (i % k) > 0:
            if processor[i - 1]:
                # front
                if i < (nmk - mk):
                    if processor[i + mk]:
                        if not processor[i + mk - 1]:
                            counter += 1
                            continue
                # right
                if (i % k) < (k - 1):
                    if processor[i + 1]:
                        counter += 1
                        continue
                # down
                if (i % mk) < (mk - k):
                    if processor[i + k]:
                        if not processor[i + k - 1]:
                            counter += 1
                            continue
        # up
        if (i % mk) >= k:
            if processor[i - k]:
                # front
                if i < (nmk - mk):
                    if processor[i + mk]:
                        if not processor[i + mk - k]:
                            counter += 1
                            continue
                # right
                if (i % k) < (k - 1):
                    if processor[i + 1]:
                        if not processor[i - k + 1]:
                            counter += 1
                            continue
                # down
                if (i % mk) < (mk - k):
                    if processor[i + k]:
                        counter += 1
                        continue
    print(counter)


main()