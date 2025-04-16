import sys
sys.stdin = open('input.txt', 'r')

def dfs(root, k):
    global cnt, real_root
    if root == k:
        return

    if not li[root]:
        cnt += 1
        return

    for next_node in li[root]:
        if visited[next_node] == 1:
            return

        visited[next_node] = 1
        dfs(next_node, k)
        if len(li[root]) == 1 and li[root][0] == k:
            cnt += 1


n = int(input())
arr = list(map(int, input().split()))
k = int(input())
visited = [0] * n
li = [[] for _ in range(n)]

for i in range(n):
    if arr[i] == -1:
        real_root = i
    else:
        li[arr[i]].append(i)

cnt = 0

dfs(real_root, k)
print(cnt)