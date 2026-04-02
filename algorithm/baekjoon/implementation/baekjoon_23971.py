# w는 가로, h는 세로
# 세로로 n칸, 가로로 m칸 띄우고 앉아야 하는 상황.
# 각 숫자는 최대 50,000
# 최대 수용 인원

# 풀이 방법
# 1. 가로와 세로를 각각 m+1과 n+1로 나누어서 최대 수용 인원을 계산한다.
# 2. 가로와 세로의 최대 수용 인원을 곱하여 최대 수용 인원을 계산한다.


import sys
sys.stdin = open('input.txt', 'r')

w, h, m, n = map(int, input().split())

max_width = w //(m+1) if w % (m+1) == 0 else w //(m+1) + 1
max_length = h //(n+1) if h % (n+1) == 0 else h //(n+1) + 1

print(max_width * max_length)