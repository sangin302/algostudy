from collections import deque
import sys
sys.stdin = open("input.txt","r")


def unlock(now, answer):
    queue = deque()
    queue.append((now, []))
    visited = [0] * 10000
    visited[now] = 1

    while queue:
        a, key = queue.popleft()
        if a == answer:
            print(f'#{tc}',"".join(key))
            break
        if a * 2 < 10000:
            if visited[a * 2] == 0:
                visited[a * 2] = 1
                queue.append((a*2, key + ['D']))
        if a * 2 >= 10000:
            if visited[a * 2 % 10000] == 0:
                visited[a * 2 % 10000] = 1
                queue.append((a * 2 % 10000, key + ['D']))
        if a - 1 >= 0:
            if visited[a - 1] == 0:
                visited[a - 1] = 1
                queue.append((a - 1, key + ['S']))
        if a - 1 < 0:
            if visited[9999] == 0:
                visited[9999] = 1
                queue.append((9999, key + ['S']))
        if visited[(a//1000) + (a%1000)*10] == 0:
            queue.append(((a//1000) + (a%1000)*10, key + ['L']))
        if visited[(a//10) + (a%10)*1000] == 0:
            queue.append(((a//10) + (a%10)*1000, key + ['R']))



T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    unlock(a, b)
