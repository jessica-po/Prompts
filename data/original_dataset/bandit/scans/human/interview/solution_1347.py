from sys import stdin
from collections import defaultdict

def main():
  stdin.readline()
  num = {}
  stat = lambda word: (word.count('r'), 
      len(word), num.setdefault(word, len(num)))
  essay = list(map(stat, stdin.readline().lower().split()))
  queue = []
  for word in essay:
    queue.append(word)
  n_synonym = int(stdin.readline())
  synonym = defaultdict(list)
  for i in range(n_synonym):
    word, rep = map(stat, stdin.readline().lower().split())
    synonym[rep[2]].append(word[2])
    queue.append(rep)
  queue.sort(reverse=True)
  best = {}
  while queue:
    n_r, length, word = queue.pop()
    if word in best:
      continue
    best[word] = n_r, length
    for rep in synonym[word]:
      if rep not in best:
        queue.append((n_r, length, rep))

  sum_n_r, sum_len = 0, 0
  for n_r, length, word in essay:
    n_r, length = best[word]
    sum_n_r += n_r
    sum_len += length
  print(sum_n_r, sum_len)

def __starting_point():
  main()
__starting_point()