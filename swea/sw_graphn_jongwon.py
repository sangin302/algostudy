import sys
sys.stdin = open("input.txt", "r")


def in_order(n):        # 중위 순회
    if n == -1:
        return
    in_order(left[n])
    print(n, end=" ")
    in_order(right[n])


def pre_order(n):       # 전위 순회
    if n == -1:
        return
    print(n, end=" ")
    pre_order(left[n])
    pre_order(right[n])


def post_order(n):      # 후위 순회
    if n == -1:
        return
    post_order(left[n])
    post_order(right[n])
    print(n, end=" ")


T = int(input())
for tc in range(1, T + 1):
    num = int(input())
    arr = [list(map(int, input().split())) for _ in range(num)]
    root = 1
    left = [0] * (num + 1)
    right = [0] * (num + 1)
    for i in range(num):
        left[arr[i][0]] = arr[i][1]
        right[arr[i][0]] = arr[i][2]
    print(f'#{tc}')
    in_order(root)
    print()
    pre_order(root)
    print()
    post_order(root)
    print()