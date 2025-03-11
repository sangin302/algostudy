import sys
sys.stdin = open("input.txt","r")
from collections import deque

def control(start, end):
    visited = [0] * 100001
    visited[start] = 1
    queue = deque()
    queue.append((start, 0))


    while queue:
        a, cnt = queue.popleft()

        if a == end:
            print(f'#{tc} {cnt}')
            return

        if a * 2 <= 100000:
            if visited[a * 2] == 0:
                queue.append((a*2, cnt + 1))
                visited[a*2] = 1
        if a - 1 >= 0:
            if visited[a - 1] == 0:
                queue.append((a - 1, cnt + 1))
                visited[a - 1] = 1
        if a + 1 <= 100000:
            if visited[a + 1] == 0:
                queue.append((a + 1, cnt + 1))
                visited[a + 1] = 1
        if a != 0:
            if visited[a // 2] == 0:
                queue.append((int(a//2), cnt + 1))
                visited[a // 2] = 1

T = int(input())
for tc in range(1, T+1):
    s, d = map(int, input().split())
    control(s, d)