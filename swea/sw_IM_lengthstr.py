import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    k = int(input())
    arr = list(input().strip())
    box = []
    max_value = -1
    for i in range(len(arr)):
        if arr[i] == 'A':
            box.append(i)

    if len(box) < k:
        print(f'#{tc} {0}')

    elif len(box) == k:
        print(f'#{tc} {box[-1] - box[0]}')

    else:
        for j in range(len(box) - k):
            max_value = max(max_value, box[j+k-1] - box[j])
        print(f'#{tc} {max_value}')