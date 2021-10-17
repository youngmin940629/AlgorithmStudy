import sys;sys.stdin = open('2479.txt')

from collections import deque

def check(a:str, b:str):
    cnt = 0
    for i in range(K):
        if a[i] != b[i]:
            cnt += 1
            if cnt >= 2:
                return False
    return True

N, K = map(int, input().split())
arr = [0]
for i in range(N):
    arr.append(input())
A, B = map(int, input().split())

visited = [0] * (N+1)

def BFS(x):
    Q = deque()
    Q.append((x, [x]))
    visited[x] = 1
    while Q:
        n, l = Q.popleft()
        for i in range(1, N+1):
            if not visited[i] and check(arr[n], arr[i]):
                visited[i] = 1
                Q.append((i, l+[i]))
                if i == B:
                    return l+[i]
    return [-1]

print(*BFS(A))