T = int(input())
for tc in range(1, T+1):
    n, *arr = list(map(int, input().split()))
    aver = 0
    for i in arr:
        aver += i
    aver /= n
    cnt = 0
    for j in arr:
        if j>aver:
          cnt += 1
    print(f'{round(cnt/n * 100, 3)}%')