#import sys
#sys.stdin = open('s.txt','r')

# 효율 개박살 통과 ㅋㅋ
dr = [0, 1, 0, -1, 1, -1, 1, -1]
dc = [1, 0, -1, 0, 1, -1, -1, 1]
def wave(r, c, n):
    global rear
    for k in range(8):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < M:
            if 0 < arr[nr][nc] < 9:
                arr[nr][nc] -= 1
                if arr[nr][nc] == 0:
                    rear += 1
                    Q[rear] = (nr, nc, n+1)
                
N, M = map(int, input().split())
arr = [[0]*M for _ in range(N)]
Q = [0] * M * N * 9
front = -1
rear = -1

for r in range(N):
    sen = input()
    for c in range(M):
        if sen[c] == '.':
            arr[r][c] = 0
            rear += 1
            Q[rear] = (r, c, 0)
        else:
            arr[r][c] =int(sen[c])


while front != rear:
    front += 1
    wave(Q[front][0], Q[front][1], Q[front][2])

print(Q[front][2])