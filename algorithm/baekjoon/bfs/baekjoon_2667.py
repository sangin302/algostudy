import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
# 각 줄이 "01101" 같은 문자열로 들어오므로, 문자 하나씩 int로 변환
grid = [list(map(int, input().strip())) for _ in range(N)]

dirs = [(1,0), (-1,0), (0,1), (0,-1)]  # 우, 좌, 하, 상
sizes = []

for r in range(N):
    for c in range(N):
        if grid[r][c] == 1:
            # 새로운 단지 발견 → BFS 시작
            q = deque([(r, c)])
            grid[r][c] = 0   # 방문 처리(0으로 바꿔 재방문 방지)
            count = 0

            while q:
                y, x = q.popleft()
                count += 1
                for dx, dy in dirs:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < N and grid[ny][nx] == 1:
                        grid[ny][nx] = 0
                        q.append((ny, nx))

            sizes.append(count)

# 출력
print(len(sizes))
for s in sorted(sizes):
    print(s)
