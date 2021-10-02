import sys; sys.stdin = open('BOJ_7576_토마토.txt','r')

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    lst = [list(map(int,input().split())) for _ in range(m)]
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    for i in range(m):
        for j in range(n):
            if lst[i][j] == 1:
                r = i
                c = j
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0<=nr<m and 0<=nc<n and lst[nr][nc] == 1:
                    pass
                elif 0<=nr<m and 0<=nc<n and lst[i][j] == 0 and lst[nr][nc] == -1:
                    pass

