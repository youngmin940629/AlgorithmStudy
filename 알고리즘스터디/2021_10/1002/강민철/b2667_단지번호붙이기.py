import sys;sys.stdin = open('2667.txt')

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
def search(c, i, j):
    global res
    visited[i][j] = c
    if len(res) < c + 1:
        res += [0]
    res[c] += 1
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni <N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] == '1':
            search(c, ni, nj)

N = int(input())
arr = [input() for _ in range(N)]
visited = [[0]*N for _ in range(N)]
cnt = 0
res = [0]

for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and not visited[i][j]:
            cnt += 1
            search(cnt, i, j)

print(cnt)
for i in sorted(res[1:]):
    print(i)