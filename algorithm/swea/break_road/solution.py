'''
mId: 도로의 ID ( 1 ≤ mId ≤ 1,000,000,000 )

sCity: 도로의 출발 도시 ( 0 ≤ sCity < N )

eCity: 도로의 도착 도시 ( 0 ≤ eCity < N )

mTime: 도로의 소요 시간 ( 1 ≤ mTime ≤ 1,000 )
'''
# -- 전역변수 --
graph = [] 			# 간선 정보를 저장
edge = {}  			# id를 기반으로 시작점을 빠르게 찾기 위한 edge
ignore = set()		# 다익스트라 할 때, id를 보고 무시하기 위한 set
INF = 10 ** 9

import heapq

def dijkstra(start, end, break_id):
	N = len(graph)

	parent = [-1] * N
	dists = [INF] * N
	dists[start] = 0

	pq = [(0, start)] # 시간과 시작 정점

	while pq:
		# 시간과 시작 정점을 꺼내고
		time, u = heapq.heappop(pq)
		# 이미 더 작은 경로가 있으면 skip
		# 보통은 안들리면 dists가 무한대니까 들리게 될 것.
		if dists[u] < time:
			continue

		# 만약에 갱신이 될 수 있다면, 해당 정점에 대해 다음으로 가는 간선을 꺼내서 본다
		for v, w, ids in graph[u]:
			if ids in ignore:  # remove 된 id 제거
				continue

			# 기존에 걸리던 시간 + 지금 갱신된 시간으로 새로운 시간 생성
			new_time = time + w

			if new_time < dists[v]:
				dists[v] = new_time
				parent[v] = u
				heapq.heappush(pq, (new_time, v))
	path = []
	if dists[end] != INF:
		while end != -1:
			path.append(end)
			end = parent[end]
		path.reverse()

	return dists, path


# -- 필수 코드 --
def init(N, K, mId, sCity, eCity, mTime):
	global graph, edge, ignore
	graph = [[] for _ in range(N)]
	edge = {}
	ignore = set()

	for i in range(K):
		u = sCity[i]
		v = eCity[i]
		w = mTime[i]
		ids = mId[i]
		graph[u].append((v, w, ids))
		edge[ids] = (u, v)


def add(mId, sCity, eCity, mTime):
	u = sCity
	v = eCity
	w = mTime
	ids = mId
	graph[u].append((v, w, ids))
	edge[ids] = (u, v)

def remove(mId):
	ignore.add(mId)

def calculate(sCity, eCity):
	# 첫 다익스트라
	dists, path = dijkstra(sCity, None)

	if dists[eCity] == INF:
		return -1

	first_ans = dists[eCity]
	# 지연 시간 저장을 위한 값
	max_delay = 0

	# path에서 u, v에 대해서 해당 id를 찾음
	# 그 id를 ignore에 넣고 다익스트라.
	# 끝나고 나서 max_delay 갱싱하고
	# ignore에서 제거.
	# path u, v 끝날때 까지니까, len(path)-1 만큼만 돌면 됨

	for i in range(len(path)-1):
		u = path[i]
		v = path[i+1]

		for new_v, time, ids in graph[u]:
			if new_v == v:
				edge_id = ids
				break

		ignore.add(edge_id)

		new_dists, _ = di





	return max_delay