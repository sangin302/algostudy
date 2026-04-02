T = int(input())
for tc in range(1, T+1):
    n = int(input())
    start_y, start_x = map(int, input().split())
    end_y, end_x = map(int, input().split())

    visited = [[0] * n for _ in range(n)]
    step = [[0] * n for _ in range(n)]

    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    dx = [1, 2, 2, 1, -1, -2, -2, -1]

    def bfs(y, x):
        stack = [(y, x)]
        visited[y][x] = 1
        while stack:
            y, x = stack.pop(0)

            if y == end_y and x == end_x:
                print(step[y][x])
                return

            for i in range(8):
                n_y = y + dy[i]
                n_x = x + dx[i]

                if 0 <= n_y < n and 0 <= n_x < n and visited[n_y][n_x] == 0:
                    visited[n_y][n_x] = 1
                    step[n_y][n_x] = step[y][x] + 1
                    stack.append((n_y, n_x))

    bfs(start_y, start_x)