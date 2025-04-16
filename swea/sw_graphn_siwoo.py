from collections import deque


def find(startpoint, transfer):
    global cnt
    stack.append(startpoint)

    while stack:
        a = stack.popleft()
        for j in road[a]:
            if visited[j] != 0 or visited[a] == transfer + 1:
                continue

            stack.append(j)
            visited[j] = visited[a] + 1
            cnt += 1


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    r, k = map(int, input().split())
    visited = [0] * (n + 1)  # 방문점 표시
    visited[r] = 1
    stack = deque()
    cnt = 1

    road = [[] for _ in range(n + 1)]  # 인덱스를 기준으로 갈 수 있는 길 표시
    for i in range(m):
        road[arr[i][0]].append(arr[i][1])
        road[arr[i][1]].append(arr[i][0])

    find(r, k)
    print(f'#{tc} {cnt}')
