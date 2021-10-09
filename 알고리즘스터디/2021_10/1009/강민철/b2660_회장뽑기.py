import sys;sys.stdin = open('2660.txt')

from collections import deque

N = int(input())
adj = [[] for i in range(N+1)]
while True:
    a, b = map(int, input().split())
    if a < 0:
        break
    adj[a].append(b)
    adj[b].append(a)

chair = N-1
res = list()
for i in range(1, N+1):
    cnt = 0
    visited = [0] * (N+1)
    dq = deque()
    dq.append(i)
    visited[i] = 1
    while dq:
        v = dq.popleft()
        for w in adj[v]:
            if not visited[w]:
                visited[w] = visited[v]+1
                dq.append(w)
                if visited[w] > cnt:
                    cnt = visited[w]

    if cnt < chair:
        res = list()
        res.append(i)
        chair = cnt
    elif cnt == chair:
        res.append(i)

print(chair-1, len(res))
print(*res)