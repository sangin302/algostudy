import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
for y in range(1, n+1):
    for x in range(1, n+1):
        print(y, x)