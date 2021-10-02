import sys; sys.stdin = open('10026.txt', 'r')
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def district_general(rgb):
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and picture[nr][nc] == rgb and not visited_general[nr][nc]:
                q.append((nr, nc))
                visited_general[nr][nc] = 1
    return 1

def district_odd_eye(rb):
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and picture[nr][nc] == rb and not visited_odd_eye[nr][nc]:
                q.append((nr, nc))
                visited_odd_eye[nr][nc] = 1
    return 1



N = int(input())
picture = [list(input()) for _ in range(N)]

q = deque()

# 일반인: general
color = ['R', 'G', 'B']
num_of_general = 0
visited_general = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if picture[i][j] in color and not visited_general[i][j]:
            visited_general[i][j] = 1
            q.append((i, j))
            num_of_general += district_general(picture[i][j])

print(num_of_general, end=' ')


# 적록색약인:odd_eye
odd_eye_color = ['R', 'B']
visited_odd_eye = [[0] * N for _ in range(N)]
num_of_odd_eye = 0

# 그림 바꾸기
for i in range(N):
    for j in range(N):
        if picture[i][j] == 'G':
            picture[i][j] = 'R'

for i in range(N):
    for j in range(N):        
        if picture[i][j] in odd_eye_color and not visited_odd_eye[i][j]:
            visited_odd_eye[i][j] = 1
            q.append((i, j))
            num_of_odd_eye += district_odd_eye(picture[i][j])

print(num_of_odd_eye)