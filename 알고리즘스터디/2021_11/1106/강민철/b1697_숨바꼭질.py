import sys;sys.stdin = open('1697.txt')

from collections import deque

def BFS():
    N, K = map(int, input().split())
    dq = deque()
    dq.append(N)
    limit = 100000
    used = [0] * (limit + 1)
    t = 0
    while dq:
        for _ in range(len(dq)):
            n = dq.popleft()
            if n == K: return t
            if n-1 >= 0 and not used[n-1]:
                dq.append(n - 1)
                used[n - 1] = 1
            if n+1 <= K and not used[n+1]:
                dq.append(n + 1)
                used[n + 1] = 1
            if n*2 <= limit and not used[n*2]:
                dq.append(n * 2)
                used[n * 2] = 1
        t += 1

print(BFS())