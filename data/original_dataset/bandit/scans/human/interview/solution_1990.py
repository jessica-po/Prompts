# reproduction of solution № 66039386 by @windhunterSB
import sys


# inf = open('input.txt', 'r')
# reader = (line.rstrip() for line in inf)
reader = (s.rstrip() for s in sys.stdin)

n = int(next(reader))
operations = next(reader)

# inf.close()

left_sum = [0] * (n + 2)   # for s[:i+1]
right_sum = [0] * (n + 2)  # for s[i:][::-1]
left_min = [0] * (n + 2)   # min - validation of bracket sequence
right_min = [0] * (n + 2)  
left_max = [0] * (n + 2)   # max - depth of bracket sequence
right_max = [0] * (n + 2)
text = [0] * (n + 2)       # entered text, letters marked as 0

op_map = {'(': 1,
          ')': -1}
ans = []
i = 1  # cursor loc i >= 1
for op in operations:
    if op == 'L':
        i = max(1, i - 1)
    elif op == 'R':
        i += 1
    else:
        text[i] = op_map.get(op, 0)
        
    left_sum[i] = left_sum[i - 1] + text[i]
    left_min[i] = min(left_min[i - 1], left_sum[i])
    left_max[i] = max(left_max[i - 1], left_sum[i])
    
    right_sum[i] = right_sum[i + 1] - text[i]  # -text[i] cause of symmetry
    right_min[i] = min(right_min[i + 1], right_sum[i])
    right_max[i] = max(right_max[i + 1], right_sum[i])
    
    correct = left_min[i] >= 0 and right_min[i + 1] >= 0 and left_sum[i] == right_sum[i + 1]
    status = max(left_max[i], right_max[i + 1]) if correct else -1
    ans.append(status)
    
print(*ans)