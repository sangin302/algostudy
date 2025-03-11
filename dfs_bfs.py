import sys
sys.stdin = open('input.txt', 'r')

def pre_order(n, cnt):
    if n == -1:
        return cnt
        return

    pre_order(left[n], cnt + 1)
    pre_order(right[n], cnt + 1)


T = int(input())
for tc in range(1, T+1):
    num = int(input())

    left = [0] * (num+1)
    right = [0] * (num+1)
    for i in range(num):
        left[arr[i][0]] = arr[i][1]
        right[arr[i][0]] = arr[i][2]

    pre_order(root)
    print()

