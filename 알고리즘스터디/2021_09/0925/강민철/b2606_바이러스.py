import sys;sys.stdin = open('2606.txt')

N = int(input())
K = int(input())
adj = [[] for i in range(N+1)]

for i in range(K):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [0] * (N+1)
def search(x):
    visited[x] = 1
    for i in adj[x]:
        if not visited[i]:
            search(i)

search(1)
print(sum(visited)-1)