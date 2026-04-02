import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
li = list(map(int, input().split()))

print(min(li), max(li))
