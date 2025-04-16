import sys
sys.stdin = open('input.txt', 'r')

def dfs(k):
    for x in range(n):
        if arr[k][x] == 0:
            arr[k][x] = 2       #퀸이 들어가는 자리를 2
            a = x
            for y in range(n):
                arr[y][a] = 1
            

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]