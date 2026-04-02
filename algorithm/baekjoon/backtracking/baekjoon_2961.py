import sys
sys.stdin = open("input.txt", "r")

n = int(input())
favor = [list(map(int, input().split())) for _ in range(n)]

min_value = float('inf')

def dfs(idx, sour, bitter, count):
    global min_value
    if count > 0:
        min_value = min(min_value, abs(sour-bitter))

    for i in range(idx, n):
        s, b = favor[i]
        dfs(i+1, sour*s, bitter+b, count+1)

dfs(0, 1, 0, 0)
print(min_value)

