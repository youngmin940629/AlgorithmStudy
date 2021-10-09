import sys;sys.stdin = open('2636.txt')

from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

dq = deque()
dq.append([0, 0])
arr[0][0] = 9
tmp_dq = deque()
hour = 0
while dq or tmp_dq:
    if not dq:
        dq.extend(tmp_dq)
        cnt = len(tmp_dq)
        tmp_dq = deque()
        hour += 1
    loc = dq.popleft()
    i, j = loc[0], loc[1]
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < N and 0 <= nj < M and not arr[ni][nj]:
            arr[ni][nj] = 9
            dq.append([ni, nj])
        elif 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1:
            arr[ni][nj] = 9
            tmp_dq.append([ni, nj])

print(hour, cnt, sep='\n')