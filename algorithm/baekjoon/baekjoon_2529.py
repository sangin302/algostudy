import sys
sys.stdin = open('input.txt', 'r')

k = int(input())
rel = list(input().split())

max_result = []
min_result = []
max_store = []
min_store = []
max_start = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
min_start = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
flag = True
count = 0

for i in rel:
    if i == ">":
        if flag == True:
            a = max_start.pop()
            max_result.append(a)
            count += 1
        if flag == False:
            b = max_start.pop()
            max_result.append(b)
            while max_store:
                c = max_store.pop()
                max_result.append(c)
            flag = True
            count += 1
    if i == "<":
        b = max_start.pop()
        max_store.append(b)
        flag = False
        count += 1
    if count == k:
        d = max_start.pop()
        max_result.append(d)
        while max_store:
            c = max_store.pop()
            max_result.append(c)

print(''.join(map(str,max_result)))

flag = True
count = 0

for i in rel:
    if i == "<":
        if flag == True:
            a = min_start.pop()
            min_result.append(a)
            count += 1
        if flag == False:
            b = min_start.pop()
            min_result.append(b)
            while min_store:
                c = min_store.pop()
                min_result.append(c)
            flag = True
            count += 1
    if i == ">":
        b = min_start.pop()
        min_store.append(b)
        flag = False
        count += 1
    if count == k:
        d = min_start.pop()
        min_result.append(d)
        while min_store:
            c = min_store.pop()
            min_result.append(c)
            
print(''.join(map(str,min_result)))
