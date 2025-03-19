import sys
sys.stdin = open('input.txt', 'r')

def find_set(x):
    if x == parents[x]:
        return x

    return find_set(parents[x])

def union(x, y):
    global flag
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        flag = True
        return

    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    parents = [i for i in range(n)]
    arr = [list(map(int, input().split())) for _ in range(n)]
    li = []
    flag = False

    for y in range(n):
        for x in range(y+1, n):
           if arr[y][x] == 1:
               union(y, x)



    if flag == False:
        print(f'#{tc} STABLE')
    else:
        print(f'#{tc} WARNING')