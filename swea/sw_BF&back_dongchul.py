import sys
sys.stdin = open('input.txt', 'r')

def calculate(person, total):
    global max_value
    if total == 0:
        return

    if total < max_value:
        return

    if person == n:
        max_value = max(max_value, total)
        return max_value

    for work in range(n):
        if visited[work]:
            continue

        visited[work] = 1
        calculate(person + 1, total * arr[person][work] * 1/100)
        visited[work] = 0

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    max_value = -1

    calculate(0, 1)
    print(f'#{tc} {(max_value*100):6f}')

