import heapq
from itertools import permutations

# ===== 전역 변수 =====
N_global = 0
graph = []

INF = 10 ** 9


# ===== 내부 헬퍼 함수 (허용됨) =====
def widest_dijkstra(start):
    """
    start에서 각 도시까지 갈 수 있는
    '경로상의 최소 간선값을 최대화한 값'을 계산
    """
    dist = [0] * N_global
    dist[start] = INF

    pq = [(-INF, start)]  # max heap
    while pq:
        cur_cap, u = heapq.heappop(pq)
        cur_cap = -cur_cap

        if cur_cap < dist[u]:
            continue

        for v, limit in graph[u]:
            next_cap = min(cur_cap, limit)
            if next_cap > dist[v]:
                dist[v] = next_cap
                heapq.heappush(pq, (-next_cap, v))

    return dist


# ===== 필수 API =====
def init(N, K, sCity, eCity, mLimit):
    global N_global, graph
    N_global = N
    graph = [[] for _ in range(N)]

    for i in range(K):
        a = sCity[i]
        b = eCity[i]
        w = mLimit[i]
        graph[a].append((b, w))
        graph[b].append((a, w))


def add(sCity, eCity, mLimit):
    graph[sCity].append((eCity, mLimit))
    graph[eCity].append((sCity, mLimit))


def calculate(sCity, eCity, M, mStopover):
    stops = mStopover[:M]

    # 필요한 시작점들만 다익스트라 수행
    needed = [sCity, eCity] + stops
    needed = list(set(needed))

    dist_map = {}
    for src in needed:
        dist_map[src] = widest_dijkstra(src)

    answer = 0

    # 경유지 순열 전부 시도
    for perm in permutations(stops):
        path = [sCity] + list(perm) + [eCity]
        bottleneck = INF
        possible = True

        for i in range(len(path) - 1):
            a = path[i]
            b = path[i + 1]
            cap = dist_map[a][b]
            if cap == 0:
                possible = False
                break
            bottleneck = min(bottleneck, cap)

        if possible:
            answer = max(answer, bottleneck)

    return -1 if answer == 0 else answer