from collections import deque

def bfs():
    global result
    while q:
        loc = q.popleft()
        if loc == K:
            return visit[loc]
        else:
            for case in range(3):
                if case == 0:
                    next = loc - 1
                if case == 1:
                    next = loc + 1
                if case == 2:
                    next = loc * 2
                if 0 <= next < 100001 and not visit[next]:
                    visit[next] = visit[loc] + 1
                    q.append((next))


N, K = map(int, input().split())
q = deque()
q.append((N))
visit = [0] * 100001
print(bfs())