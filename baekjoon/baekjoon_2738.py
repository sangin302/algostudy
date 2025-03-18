import sys
sys.stdin = open("input.txt", "r")  # 같은 폴더 내의 input.txt 파일 읽기

n, m = map(int, input().split())
arr_1 = [list(map(int, input().split())) for _ in range(n)]
arr_2 = [list(map(int, input().split())) for _ in range(n)]
li = []
for y in range(n):
    for x in range(m):
        li.append(arr_1[y][x] + arr_2[y][x])
    print(*li)
    li = []