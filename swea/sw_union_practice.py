import sys
sys.stdin = open('input.txt', 'r')

def find_set(x):
    # x가 집합의 대표자다 == x와 parents[x]가 같다
    if x == parents[x]:
        return x

    # # 기본적인 경로 압축 코드
    # ref = find_set(parents[x]) # 집합의 대표자 검색
    # parents[x] = ref           # x의 부모를 대표자로
    # return ref

    # 위 3줄을 줄인 코드
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    # x 그룹과, y 그룹을 합치는 과정
    #   -> 대표자끼리 합쳐야 한다
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:  # 이미 같은 그룹이라면?
        return

    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = []

    # 1. make_set (자기 자신을 집합의 대표자로 설정)
    parents = [i for i in range(N + 1)]
    print(parents)
    for _ in range(M):
        q, x, y = map(int, input().split())
        # x, y 가 같은 집합인지 확인
        if q == 0:
            if find_set(x) == find_set(y):
                result.append('YES')
            else:
                result.append('NO')
        # x, y 를 연결
        else:
            union(x, y)

    print(f'#{tc}', *result)