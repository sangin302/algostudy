import sys
sys.stdin = open('input.txt', 'r')

def subset(arr, index, total):
    global min_value
    if index == n:
        if total >= b:
            min_value = min(min_value, total)
        return
    subset(arr, index + 1, total + arr[index])
    subset(arr, index + 1, total)

T = int(input())
for tc in range(1, T + 1):
    n, b = map(int, input().split())
    worker = list(map(int, input().split()))
    min_value = 2000001
    subset(worker, 0, 0)
    print(f'#{tc} {min_value - b}')
