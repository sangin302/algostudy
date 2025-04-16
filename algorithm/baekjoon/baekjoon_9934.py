import sys
sys.stdin = open('input.txt', 'r')

def in_order(root):
    in_order(left)
    print(root)
    in_order(right)


k = int(input())
arr = list(map(int, input().split()))
li = [0] * (2**k)

