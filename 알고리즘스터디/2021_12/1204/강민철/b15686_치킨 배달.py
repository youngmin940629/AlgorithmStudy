import sys;sys.stdin = open('15686.txt')

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

homes = []
chickens = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            homes.append((i, j))
        elif arr[i][j] == 2:
            chickens.append((i, j))

lst = [[] for _ in range(len(homes))]
for i in range(len(homes)):
    for j in range(len(chickens)):
        d = abs(homes[i][0] - chickens[j][0]) + abs(homes[i][1] - chickens[j][1])
        lst[i].append(d)

result = 987654321
def comb(n, k, s, lev, exc):
    if lev >= k:
        res = 0
        for j in range(len(homes)):
            mini = 987654321
            for i in range(len(chickens)):
                if exc & 1<<i: continue
                mini = min(mini, lst[j][i])
            res += mini
        global result
        if res < result:
            result = res
        return
    for i in range(s, n):
        exc |= 1<<i
        comb(n, k, i+1, lev+1, exc)
        exc ^= 1<<i

comb(len(chickens), len(chickens)-M, 0, 0, 0)
print(result)