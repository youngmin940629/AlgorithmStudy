from collections import deque

def solve():
    T = int(input())
    for tc in range(T):
        w, h = map(int, input().split())
        arr = [input() for _ in range(h)]

        visited = [[0] * w for _ in range(h)]
        dq_fire = deque()
        dq_sg = deque()
        for i in range(h):
            for j in range(w):
                if arr[i][j] == '*':
                    dq_fire.append([i, j])
                    visited[i][j] = 2
                elif arr[i][j] == '#':
                    visited[i][j] = 3
                elif not dq_sg and arr[i][j] == '@':
                    dq_sg.append([i, j])
                    visited[i][j] = 1
                    ii = i
                    jj = j

        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]
        cnt = 0
        flag = 0
        if ii == 0 or ii == h - 1 or jj == 0 or jj == w - 1:
            flag = 1
        while dq_sg and not flag:
            tmp_dq_fire = deque()
            while dq_fire:
                loc = dq_fire.popleft()
                i = loc[0]
                j = loc[1]
                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]
                    if 0 <= ni < h and 0 <= nj < w and visited[ni][nj] < 2:
                        visited[ni][nj] = 2
                        tmp_dq_fire.append([ni, nj])
            dq_fire.extend(tmp_dq_fire)
            cnt += 1
            tmp_dq_sg = deque()
            while dq_sg:
                loc = dq_sg.popleft()
                i = loc[0]
                j = loc[1]
                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]
                    if 0 <= ni < h and 0 <= nj < w and visited[ni][nj] < 1:
                        visited[ni][nj] = 1
                        tmp_dq_sg.append([ni, nj])
                        if ni == 0 or ni == h-1 or nj == 0 or nj == w-1:
                            flag = 1
                            break
                if flag:
                    break
            if flag:
                break
            dq_sg.extend(tmp_dq_sg)


        if flag:
            print(cnt+1)
        else:
            print('IMPOSSIBLE')

solve()