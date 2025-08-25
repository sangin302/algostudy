import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
stack = [[0] * 100 for _ in range(100)]
for _ in range(t):
    a, b= map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            stack[i][j] = 1

result = sum(line.count(1) for line in stack)
print(result)

