import sys;sys.stdin = open('1941.txt')

arr = [input() for _ in range(5)]
res = 0
visited = 0
check = set()

di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)
def DFS(i, j, k, cnt:int, v):
    n = i*5+j
    v = v | 1<<n
    if arr[i][j] == 'S': cnt += 1
    if k - cnt > 3: return
    if k >= 7:
        if v not in check:
            global res
            res += 1
            check.add(v)
        return
    m = len(bin(v))
    for b in range(m-2):
        if not v & 1<<b: continue
        y, x = b // 5, b % 5
        for d in range(4):
            ni, nj = y+di[d], x+dj[d]
            if ni < 0 or ni >= 5 or nj < 0 or nj >= 5: continue
            if v & 1<<(ni*5+nj): continue
            DFS(ni, nj, k+1, cnt, v)
    v = v ^ 1<<n

for i in range(5):
    for j in range(5):
        if arr[i][j] == 'S':
            DFS(i, j, 1, 0, visited)

print(res)