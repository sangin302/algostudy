import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

min_value = float('inf')

for i in range(n-7):
    for j in range(m-7):
        start_is_w = 0
        start_is_b = 0

        for y in range(8):
            for x in range(8):
                point = board[i+y][j+x]
                if (y+x) % 2 == 0:
                    if point != 'W':
                        start_is_w += 1
                    if point != 'B':
                        start_is_b += 1
                else:
                    if point != 'B':
                        start_is_w += 1
                    if point != 'W':
                        start_is_b += 1

        min_value = min(min_value, start_is_w, start_is_b)

print(min_value)

