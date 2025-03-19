import sys
sys.stdin = open('input.txt', 'r')

def find_set(x):
    if x == parents[x-65]:
        return x

    return find_set(parents[x-65])

def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y

def war(x, y):
    war_x = find_set(x)
    war_y = find_set(y)

    if war_x:
        pass



T = int(input())
for tc in range(1, T+1):
    n = int(input())
    people = list(map(int, input().split()))
    peoples = {}
    parents = [i for i in range(n)]
    for i in range(65, 65 + n):
        peoples[i] = people[i-65]
    print(peoples)
    stat = int(input())
    for _ in range(stat):
        q, a, b = input().split()
        if q == 'alliance':
            union(ord(a), ord(b))
        else:
            pass
