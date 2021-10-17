from collections import deque

def BFS():
    N = int(input())
    x, y = map(int, input().split())
    M = int(input())
    adj = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)

    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    dq = deque()
    dq.append(x)
    visited[x] = 1
    while dq:
        v = dq.popleft()
        for w in adj[v]:
            if not visited[w]:
                visited[w] = visited[v] + 1
                dq.append(w)
            if w == y:
                return visited[y]-1
    return -1

print(BFS())