import sys
sys.stdin = open("input.txt", "r")

def find(start_x, start_y, cnt):
    global result
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]

    if cnt == 6:
        if ''.join(map(str, number)) not in visited:
            visited[''.join(map(str, number))] = 1
            result += 1
        return

    for k in range(4):
        ny = start_y + dy[k]
        nx = start_x + dx[k]

        if 0 <= ny < 4 and 0 <= nx < 4:
            number.append(arr[ny][nx])
            find(ny, nx, cnt + 1)
            number.pop()

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    number = []
    visited = {}

    result = 0
    for y in range(4):
        for x in range(4):
            number = [arr[y][x]]
            find(y, x, 0)

    print(f'#{tc} {result}')
