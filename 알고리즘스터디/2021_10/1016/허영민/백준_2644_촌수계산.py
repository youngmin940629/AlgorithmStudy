from collections import deque

def bfs():
    visited = [0] * (n+1)
    while q:
        a, b, cnt = q.popleft()
        visited[b] = 1
        if a == b:
            return cnt
        else:
            if child[b]:
                for value in child[b]:
                    if not visited[value]:
                        q.append((a, value, cnt+1))
            if p[b] != 0:
                if not visited[p[b]]:
                    q.append((a, p[b], cnt+1))
    return -1

n = int(input())
a, b = map(int,input().split())
m = int(input())
p = [0] * (n+1)
child = dict()
for i in range(n+1):
    child[i] = []
for _ in range(m):
    x, y = map(int, input().split())
    p[y] = x
    child[x].append(y)
q = deque()
q.append((a,b,0))
print(bfs())