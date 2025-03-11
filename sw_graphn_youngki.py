import sys
sys.stdin = open("input.txt","r")
from collections import deque

def bfs(s, e):
    stack.append((s,0))

    while stack:
        value, cnt = stack.popleft()
        visited[value] = 1
        if value == e:
            print(f'#{tc} {cnt}')
            break
        if value >= 1:
            if visited[value-1] == 0:
                stack.append((value-1, cnt + 1))
        if value * 2 < 100001:
            if visited[value * 2] == 0:
                stack.append((value*2, cnt + 1))
        if value < 100000:
            if visited[value + 1] == 0:
                stack.append((value+1, cnt + 1))


T = int(input())
for tc in range(1, T+1):
    s, e = map(int, input().split())
    stack = deque()
    visited = [0]*100001
    bfs(s, e)

