import sys;sys.stdin = open('17135.txt')

from collections import deque

N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for _ in range(N):
    if sum(arr[_]):
        R = _
        break
arc = deque()
res = 0

di = (0, -1, 0)
dj = (-1, 0, 1)
def BFS(dq: deque, eli: deque, mat):
    visited = 1<<(dq[0][0]*N + dq[0][1])
    for d in range(D):
        for k in range(len(dq)):
            y, x = dq.popleft()
            if mat[y][x] == 1:
                eli.append((y, x))
                return
            for p in range(3):
                ny, nx = y+di[p], x+dj[p]
                if ny >= 0 and 0 <= nx < M and not visited & 1<<(ny*N + nx):
                    dq.append((ny, nx))
                    visited |= 1<<(ny*N + nx)

def play(cnt):
    mat = [lst[:] for lst in arr]
    eli = deque()
    tmp = deque(arc)
    for __ in range(N-R):
        for _ in range(len(tmp)):
            i, j = tmp.popleft()
            dq = deque()
            dq.append((i, j))
            BFS(dq, eli, mat)
            tmp.append((i-1, j))
        while eli:
            y, x = eli.popleft()
            if mat[y][x] == 1:
                mat[y][x] = 0
                cnt += 1
    return cnt

def comb(m, r, s, lev):
    if lev == r:
        global res
        res = max(res, play(0))
        return
    for x in range(s, m-r+1+lev):
        arc.append((N-1, x))
        comb(m, r, x+1, lev+1)
        arc.pop()

comb(M, 3, 0, 0)
print(res)