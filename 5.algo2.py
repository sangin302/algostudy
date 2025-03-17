import sys
sys.stdin = open('input.txt', 'r')


def pre_order(t):
    if t == -1:
        return ""
    return arr[t] + pre_order(left[t]) + pre_order(right[t])


def in_order(t):
    if t == -1:
        return ""
    return in_order(left[t]) + arr[t] + in_order(right[t])


def post_order(t):
    if t == -1:
        return ""
    return post_order(left[t]) + post_order(right[t]) + arr[t]


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    li = list(map(str, input().split()))  # 문자열로 저장 (2진수 처리하기 위함)
    arr = [0]
    for k in range(n):
        arr.append(li[k])

    left = [-1] * (n + 1)
    right = [-1] * (n + 1)

    for i in range(1, n//2 + 1):
        left[i] = i * 2
        if len(arr) - 1 >= i * 2 + 1:
            right[i] = i * 2 + 1

    a = int(pre_order(1), 2)
    b = int(in_order(1), 2)
    c = int(post_order(1), 2)

    max_value = max(a, b, c)
    print(f'#{tc} {max_value}')
