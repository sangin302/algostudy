import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
bucket = [0] * (n+1)
for _ in range(m):
    i, j, k = map(int, input().split())
    for p in range(i, j+1):
        bucket[p] = k
print(*bucket[1:])