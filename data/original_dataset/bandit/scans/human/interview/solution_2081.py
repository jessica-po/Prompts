#taken from https://stackoverflow.com/questions/30698441/optimal-way-to-find-sums-of-all-contiguous-sub-arrays-max-difference
def max_sums(d):
    stack = [(-1, float('inf'))]
    sum_ = 0
    for i, x in enumerate(d):
        while x > stack[-1][1]:
            prev_i, prev_x = stack.pop()
            prev_prev_i, prev_prev_x = stack[-1]
            sum_ += prev_x * (i - prev_i) * (prev_i - prev_prev_i)
        stack.append((i, x))
    while len(stack) > 1:
        prev_i, prev_x = stack.pop()
        prev_prev_i, prev_prev_x = stack[-1]
        sum_ += prev_x * (len(d) - prev_i) * (prev_i - prev_prev_i)
    return sum_

def max_differences_sum(d):
    return max_sums(d) + max_sums([-x for x in d])

n=int(input())
l=list(map(int,input().split()))
print(max_differences_sum(l))