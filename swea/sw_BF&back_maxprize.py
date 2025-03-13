import sys
sys.stdin = open('input.txt','r')

# 완전 탐색을 해야한다
# 모든 자리의 숫자를 각각 바꿔 주면서 비교
#  -> 방문 처리를 해주어야 한다
# 문제 조건의 교환 횟수에 도달하면 최대값 비교 후 종료

def dfs(now_level):
    global max_value
    if now_level == finish_level:
        max_value = max(max_value, int(''.join(num)))
        return
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            num[i], num[j] = num[j], num[i]

            str_num = ''.join(num)
            if visited.get((now_level, int(str_num)))is None:
                visited[(now_level, int(str_num))] = 1
                dfs(now_level + 1)

            num[i], num[j] = num[j], num[i]

T = int(input())
for tc in range(1, T+1):
    num, finish_level = input().split()
    num = list(num)
    finish_level = int(finish_level)
    # 방문 처리는, 각 level 내에서의 중복을 막아주기 위함
    visited = {}
    max_value = -1
    dfs(0)
    print(f'#{tc} {max_value}')