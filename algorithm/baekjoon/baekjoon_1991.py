import sys
sys.stdin = open('input.txt', 'r')

def pre_order(root):
    if root == '.':
        return
    print(root, end='')
    pre_order(dict[root][0])
    pre_order(dict[root][1])


def in_order(root):
    if root == '.':
        return
    in_order(dict[root][0])
    print(root, end='')
    in_order(dict[root][1])


def post_order(root):
    if root == '.':
        return
    post_order(dict[root][0])
    post_order(dict[root][1])
    print(root, end='')


n = int(input())
arr = [list(input().split()) for _ in range(n)]

dict = {}

for i in range(n):
    dict[arr[i][0]] = [arr[i][1], arr[i][2]]

pre_order('A')
print()
in_order('A')
print()
post_order('A')