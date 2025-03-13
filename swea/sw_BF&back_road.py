import sys
import heapq

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline




def dijkstra(n, arr):
    # 최소 복구 비용 저장 (무한대 초기화)
    INF = float('inf')
    cost = [[INF] * n for _ in range(n)]

    # 우선순위 큐 (최소 힙)
    pq = []

    # 시작 위치 (0,0) 설정, 초기 복구 비용 = arr[0][0]
    heapq.heappush(pq, (arr[0][0], 0, 0))  # (누적 복구 비용, x좌표, y좌표)
    cost[0][0] = arr[0][0]

    while pq:
        current_cost, x, y = heapq.heappop(pq)

        # 최적 비용이 아닌 경우 스킵
        if cost[x][y] < current_cost:
            continue

        # 상, 하, 좌, 우 이동 방향 정의
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        # 상하좌우 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 격자 범위 체크
            if 0 <= nx < n and 0 <= ny < n:
                new_cost = current_cost + arr[nx][ny]

                # 기존 비용보다 작다면 갱신 후 큐에 삽입
                if new_cost < cost[nx][ny]:
                    cost[nx][ny] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny))

    # 도착점 (n-1, n-1) 의 최소 복구 비용 반환
    return cost[n - 1][n - 1]


# 테스트 케이스 실행
T = int(input().strip())
for tc in range(1, T + 1):
    n = int(input().strip())
    arr = [list(map(int, input().strip())) for _ in range(n)]

    result = dijkstra(n, arr)
    print(f"#{tc} {result}")
