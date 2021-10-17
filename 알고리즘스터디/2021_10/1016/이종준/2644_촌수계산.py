import sys
sys.stdin = open('input.txt', 'r')

def counting(v):
    for w in range(N + 1):
        if arr[v][w] == 1 and not visited[w]:
            visited[w] = visited[v] + 1
            counting(w)


# 정점의 수
N = int(input())
# 촌수 계산할 서로 다른 두 사람
C, P = map(int, input().split())

# 인접리스트
arr = [[0] * (N + 1) for _ in range(N + 1)]

#간선의 수
E = int(input())

# 간선정보 인접리스트에 저장
for _ in range(E):
    s, e = map(int, input().split())
    arr[s][e] = 1
    arr[e][s] = 1

# 방문리스트
visited = [0] * (N + 1)
visited[C] = 1
counting(C)
print(visited[P] - 1)