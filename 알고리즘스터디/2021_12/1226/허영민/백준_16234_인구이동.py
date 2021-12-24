from collections import deque

def division(check_list):
    people_sum = 0
    for x,y in check_list:
        people_sum += arr[x][y]
    people_division = people_sum // len(check_list)
    for x,y in check_list:
        arr[x][y] = people_division
    return

def check():
    global result
    cnt = 0
    division_list = []
    visited = [0] * (N * N)
    for x in range(N):
        for y in range(N):
            if not visited[x * N + y]:
                visited[x * N + y] = 1
                tmp = []
                tmp.append((x,y))
                q.append((x,y))
                while q:
                    c, r = q.popleft()
                    for dir in range(4):
                        nc, nr = c + dx[dir], r + dy[dir]
                        if 0 <= nc < N and 0 <= nr < N and not visited[nc * N + nr]:
                            if L <= abs(arr[c][r] - arr[nc][nr]) <= R:
                                visited[nc*N + nr] = 1
                                tmp.append((nc,nr))
                                q.append((nc,nr))
                division_list.append(tmp)
    for check_list in division_list:
        if len(check_list) > 1:
            division(check_list)
            cnt += 1
    return cnt


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = 0
q = deque()
while check():
    result += 1
print(result)