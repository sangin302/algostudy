from collections import defaultdict
import sys
sys.stdin = open('input.txt', 'r')

lis = list(input().strip())
li = []
for i in lis:
    li.append(i.upper())
counts = {}
for i in li:
    counts[i] = counts.get(i, 0) + 1

max_val = max(counts.values())
pro = [k for k, v in counts.items() if v == max_val]

if len(pro) > 1:
    print('?')
else:
    print(pro[0].upper())


# pro = [k for k, v in counts]