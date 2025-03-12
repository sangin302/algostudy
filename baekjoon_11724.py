import sys
sys.stdin = open("input.txt", "r")

def dfs(d):
    for k in li[d]:
        if visited[k] == 1:
            continue
        visited[k] = 1
        dfs(k)


n, m = map(int, input().split())
li = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    li[a].append(b)
    li[b].append(a)

for j in range(1, n + 1):
    if visited[j] == 0:
        visited[j] = 1
        dfs(j)
        cnt += 1

print(cnt)

