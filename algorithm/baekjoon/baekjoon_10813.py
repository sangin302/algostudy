import sys
sys.stdin = open('input.txt','r')

n, m = map(int, input().split())
bucket = [0] * (n+1)
for i in range(1, n+1):
    bucket[i] = i
wait = 0
for _ in range(m):
    k, p = map(int, input().split())
    wait = bucket[k]
    bucket[k] = bucket[p]
    bucket[p] = wait
print(*bucket[1:])
