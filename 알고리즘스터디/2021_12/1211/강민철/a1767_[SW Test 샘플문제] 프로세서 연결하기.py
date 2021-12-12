import sys;sys.stdin = open('1767.txt')

from collections import  deque

def solve(bit, lev, end, cnt, core):
    global res, ans
    if ans > core + (end-lev): return
    if ans >= core + (end-lev) and cnt >= res: return
    if lev >= end:
        if core > ans or (core >= ans and cnt < res):
            res = cnt
            ans = core
        return
    x = dq[lev]
    tmp = bit
    for i in range(x - (x % N), x):
        if tmp & 1 << i: break
        tmp |= 1 << i
    else:
        solve(tmp, lev + 1, end, cnt + (x % N), core+1)
    tmp = bit
    for i in range(x + 1, ((x // N) + 1) * N):
        if tmp & 1 << i: break
        tmp |= 1 << i
    else:
        solve(tmp, lev + 1, end, cnt + ((x // N) + 1) * N - x - 1, core+1)
    tmp = bit
    for i in range(x % N, x, N):
        if tmp & 1 << i: break
        tmp |= 1 << i
    else:
        solve(tmp, lev + 1, end, cnt + x // N, core+1)
    tmp = bit
    for i in range(x + N, N ** 2, N):
        if tmp & 1 << i: break
        tmp |= 1 << i
    else:
        solve(tmp, lev + 1, end, cnt + (N - 1) - x // N, core+1)

    solve(bit, lev+1, end, cnt, core)

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dq = deque()

    bit = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                loc = i*N+j
                bit |= 1<<loc
                if 0 < i < N-1 and 0 < j < N-1:
                    dq.append(loc)

    res = N**2
    ans = 0
    solve(bit, 0, len(dq), 0, 0)
    print(f'#{tc+1} {res}')