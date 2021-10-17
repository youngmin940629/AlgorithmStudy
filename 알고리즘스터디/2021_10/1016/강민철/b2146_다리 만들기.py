import sys;sys.stdin = open('2146.txt')

from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
edge = set()
visited = [[0] * N for _ in range(N)]
cnt = 0
dq = deque()
for i in range(N):
    for j in range(N):
        if arr[i][j] and not visited[i][j]:
            cnt += 1
            dq = deque()
            dq.append([i, j])
            arr[i][j] = cnt
        while dq:
            loc = dq.popleft()
            i, j = loc[0], loc[1]
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    arr[ni][nj] = cnt
                    dq.append([ni, nj])
                elif 0 <= ni < N and 0 <= nj < N and not arr[ni][nj]:
                    edge.add((i, j))

bridge = N*N
while edge:
    loc = edge.pop()
    i, j = loc[0], loc[1]
    n = arr[i][j]
    dq = deque()
    dq.append([i, j])
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1
    while dq:
        loc = dq.popleft()
        i, j = loc[0], loc[1]
        if visited[i][j] > bridge:
            break
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < N and not arr[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = visited[i][j] + 1
                dq.append([ni, nj])
            elif 0 <= ni < N and 0 <= nj < N and arr[ni][nj] and arr[ni][nj] != n:
                tmp_bridge = visited[i][j]
                if tmp_bridge < bridge:
                    bridge = tmp_bridge

print(bridge-1)