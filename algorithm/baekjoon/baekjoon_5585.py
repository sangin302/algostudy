def find(b, cnt):
    if b == 0:
        return cnt
    elif b >= 500:
        b -= 500
        return find(b, cnt + 1)
    elif b >= 100:
        b -= 100
        return find(b, cnt + 1)
    elif b >= 50:
        b -= 50
        return find(b, cnt + 1)
    elif b >= 10:
        b -= 10
        return find(b, cnt + 1)
    elif b >= 5:
        b -= 5
        return find(b, cnt + 1)
    elif b >= 1:
        b -= 1
        return find(b, cnt + 1)

n = int(input())
b = 1000 - n

result = find(b, 0)
print(result)