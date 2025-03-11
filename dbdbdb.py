T = int(input())
for _ in range(T):
    arr = list(input().strip())
    cnt = 0
    total = 0
    for i in arr:
        if i == 'O':
            cnt += 1
            total += cnt
        if i == 'X':
            cnt = 0
    print(total)