N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort()
line = tuple(map(lambda x: x[1], arr))

V = [1] * N
for i in range(N-1):
    for j in range(i, N):
        if line[i] < line[j] and V[j] < V[i]+1:
            V[j] = V[i]+1
            
print(N - max(V))