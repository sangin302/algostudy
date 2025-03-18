
def find(start):


n = int(input())
li = [[] for _ in range(n)]
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        if a[j] == 1:
            li[i].append(j)
for k in range(n):
    find(k)
