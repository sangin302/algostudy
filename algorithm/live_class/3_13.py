import sys
sys.stdin = open('input.txt', 'r')

import heapq
def prim(tax):
    pq = [(0, 0)]           # (비용, 노드) 형태로 저장
    visited = [0] * n       # 방문 여부를 기록
    min_cost = 0            # 최소 비용

    dist = [float('inf')] * n
    dist[0] = 0

    while pq:
        # cost가 가장 저렴한 후보부터 나온다
        cost, node = heapq.heappop(pq)
        if visited[node]:
            continue

        visited[node] = 1
        min_cost += cost

        for next_node in range(n):
            if visited[next_node]:
                continue

            # (x좌표 차이)² + (y좌표 차이)² * tax
            new_cost = ((x_list[next_node] - x_list[node]) ** 2 + (y_list[next_node] - y_list[node]) ** 2) * tax

            # 기본보다 작은 비용으로 올 경우만 pq에 넣자
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(pq, (new_cost , next_node))

    return round(min_cost)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    tax = float(input())

    result = prim(tax)
    print(f'#{tc} {result}')