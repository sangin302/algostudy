T = int(input())

def tree_height():
    n = int(input())
    trees = list(map(int, input().split()))
    day = 1

    while trees.count(max(trees)) < n:
        stack = list(set(sorted(trees)))
        biggest = stack.pop()

        while stack:
            target = stack.pop()

            if target == biggest:
                continue

            a = trees.index(target)

            if day % 2 == 0 :
                if biggest >= target + 2:
                    trees[a] += 2
                    day += 1
                    break
                elif biggest == target + 1:
                    if stack:
                        continue
                    else:
                        day += 1


            if day % 2 == 1:
                if biggest == target + 2:
                    if target == min(trees):
                        if trees.count(target) > 1:
                            trees[a] += 1
                            dat += 1
                            break
                        else:
                            day += 1
                            break
                    else:
                        continue

                elif biggest >= target + 1:
                    trees[a] += 1
                    day += 1
                    break
        return day

for k in range(1, T+1):
    print(f'#{k} {tree_height()-1}')