path = []
def recur():
    if len(path) == 4:
        return
    for i in range(4):
        path.append(i)
        print(path)
        recur()
        path.pop()

recur()