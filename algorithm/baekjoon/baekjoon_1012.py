import sys
from collections import deque

input = sys.stdin.readline

T = int(input().strip())
DIRS = [(1,0), (-1,0), (0,1), (0,-1)]  # (dx, dy) = (가로, 세로)

for _ in range(T):
    M, N, K = map(int, input().split())  # M: 가로(열), N: 세로(행)
    cabbages = set()
    for _ in range(K):
        x, y = map(int, input().split())  # x는 0~M-1, y는 0~N-1
        cabbages.add((x, y))

    visited = set()
    worms = 0

    for start in cabbages:
        if start in visited:
            continue

        # 새로운 묶음 발견 → BFS로 같은 묶음을 싹 방문
        worms += 1
        q = deque([start])
        visited.add(start)

        while q:
            x, y = q.popleft()
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if (nx, ny) in cabbages and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append((nx, ny))

    print(worms)
