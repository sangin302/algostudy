T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = list(map(int, input().strip()))
    find = []
    max_value = -1
    for i in range(n):
        if arr[i] == 1:
            find.append(i)

    if len(find) < k:
        print(f'#{tc} 0')

    elif len(find) == k:
        print(f'#{tc} {len(find)+1}')

    else:
        for j in range(len(find)-k + 1):
            t = find[j+k-1]-find[j]
            max_value = max(max_value, t)
        print(f'#{tc} {max_value+1}')