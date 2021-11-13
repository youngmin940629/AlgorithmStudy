import sys;sys.stdin = open('7562.txt')

from collections import deque

di = (-2, -1, 1, 2, 2, 1, -1, -2)
dj = (1, 2, 2, 1, -1, -2, -2, -1)

def BFS():
    dq = deque()
    dq.append((si, sj))
    visited[si][sj] = 1
    if si == ei and sj == ej: return 0
    t = 0
    while dq:
        i, j = dq.popleft()
        for d in range(8):
            ni, nj = i+di[d], j+dj[d]
            if ni < 0 or ni >= l or nj < 0 or nj >= l: continue
            if visited[ni][nj]: continue
            visited[ni][nj] = visited[i][j] + 1
            if ni == ei and nj == ej: return visited[ni][nj] - 1
            dq.append((ni, nj))

for tc in range(int(input())):
    l = int(input())
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())

    visited = [[0]*l for _ in range(l)]

    print(BFS())