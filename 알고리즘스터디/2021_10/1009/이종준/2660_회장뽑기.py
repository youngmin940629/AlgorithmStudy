import sys; sys.stdin = open('2660.txt', 'r')
from collections import deque

def func(num):
    visited[num] = 1
    while q:
        s = q.popleft()[0]
        for w in range(1, N + 1):
            if friendmap[s][w] == 1 and not visited[w]:
                visited[w] = visited[s] + 1
                q.append([w])


N = int(input())
friendmap = [[0] * (N + 1) for _ in range(N + 1)]

while True:
    s, e = map(int, input().split())
    if s == -1:
        break
    else:
        friendmap[s][e] = 1
        friendmap[e][s] = 1

score_list = [0] * (N + 1)
q = deque()

for i in range(1, N+1):
    visited = [0] * (N + 1)
    q.append([i])
    func(i)
    score_list[i] = max(visited) - 1

min_score = 0xfffffff
for i in range(1, N + 1):
    if score_list[i] < min_score:
        min_score = score_list[i]
        
candidates = []

for i in range(1, N+1):
    if score_list[i] == min_score:        
        candidates.append(i)

print(min_score, len(candidates))
print(' '.join(map(str, candidates)))