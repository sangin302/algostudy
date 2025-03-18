import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def bfs(start_y, start_x):
    visited = [[0] * n for _ in range(n)]
    visited[start_y][start_x] = 1
    queue = deque()
    queue.append((start_y, start_x))
    fish = []
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    while queue:
        py, px = queue.popleft()
        for k in range(4):
            n_y = py + dy[k]
            n_x = px + dx[k]

            if 0 <= n_y < n and 0 <= n_x < n and visited[n_y][n_x] == 0:
                if arr[n_y][n_x] <= level:
                    visited[n_y][n_x] = visited[py][px] + 1
                    queue.append((n_y, n_x))
                    if 0 < arr[n_y][n_x] < level:
                        fish.append((visited[n_y][n_x], n_y, n_x))

    fish.sort()
    if fish:
        return fish[0]
    else:
        return False

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
for y in range(n):
    for x in range(n):
        if arr[y][x] == 9:
            arr[y][x] = 0
            start_y, start_x = y, x

time = 0
level = 2
eat = 0

while True:
    target = bfs(start_y, start_x)

    if not target:
        break

    cnt, n_y, n_x = target
    time += cnt - 1
    eat += 1
    arr[n_y][n_x] = 0
    start_y, start_x = n_y, n_x

    if eat == level:
        eat = 0
        level += 1

print(time)