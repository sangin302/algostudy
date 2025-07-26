'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def pre_order(t):
    if t:
        print(t, end=" ")
        pre_order(left[t])
        pre_order(right[t])

def in_order(t):
    if t:
        in_order(left[t])
        print(t, end=" ")
        in_order(right[t])

def post_order(t):
    if t:
        post_order(left[t])
        post_order(right[t])
        print(t, end=" ")


N = int(input())
E = N - 1

arr = list(map(int, input().split()))

left = [0] * (N+1)
right = [0] * (N+1)

par = [0] * (N+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    par[c] = p      # 자식을 인덱스로 부모 저장
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

# 이건 뭐지?#
root = 1
for i in range(1, N+1): # 부모 정점이 없으면 루트
    if par[i] == 0:
        root = i
        break
pre_order(root)

# 조상을 찾는 코드#
c = N
while par[c]!=0:        # 부모가 있으면
    c = par[c]          # 부모를 새로운 자식으로 두고
root = c                # 더이상 부모가 없으면 root
print(root)



