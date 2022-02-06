from collections import deque
X = int(input())
Q = deque()
Q.append((X, 0))
V = [0] * (X+1)

while Q:
    N, cnt = Q.popleft()
    if N == 1:
        print(cnt)
        break
    
    if not N % 3 and V[N//3] == 0:
        Q.append((N//3, cnt+1))
        V[N//3] = 1
    if not N % 2 and V[N//2] == 0:
        Q.append((N//2, cnt+1))
        V[N//2] = 1
    Q.append((N-1, cnt+1))
    V[N-1] = 1