import sys
sys.stdin = open('input.txt', 'r')
import heapq

def find(start):
    dist = [float('inf')] * n
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        money, node = heapq.heappop(pq)

        if dist[node] < money:
            continue

        for cost, next_node in arr[node]:
            new_cost = money + cost
            if dist[next_node] > new_cost:
                dist[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

    return dist[n - 1] if dist[n - 1] != float('inf') else 'impossible'

T = int(input())
for tc in range(1, T+1):
    n, t = map(int, input().split())
    arr = [[] for _ in range(n)]
    for _ in range(t):
        s, e, w = map(int, input().split())
        arr[s].append((w, e))
    result = find(0)
    print(f'#{tc} {result}')


