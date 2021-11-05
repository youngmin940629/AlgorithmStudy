def dfs(check_cnt, idx, yeon):
    global result
    global visit
    if yeon >= 4 or 25 - idx < 7 - check_cnt:
        return
    if check_cnt == 7:
        check(check_arr[0])
        visit_check = 0
        for x in range(5):
            for y in range(5):
                visit_check += visit[x][y]
        if visit_check == 7:
            result += 1
        visit = [[0] * 5 for _ in range(5)]
        return
    x = idx // 5
    y = idx % 5
    check_arr.append(idx)
    if students[x][y] == 'Y':
        dfs(check_cnt+1, idx+1, yeon+1)
    elif students[x][y] == 'S':
        dfs(check_cnt+1, idx+1, yeon)
    check_arr.pop()
    dfs(check_cnt, idx+1, yeon)

def check(s):
    x = s // 5
    y = s % 5
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < 5 and 0 <= ny < 5:
            if not visit[nx][ny]:
                if ((nx * 5) + ny) in check_arr:
                    visit[nx][ny] = 1
                    check(((nx * 5) + ny))


students = [list(input()) for _ in range(5)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visit = [[0] * 5 for _ in range(5)]
result = 0
check_arr = []
dfs(0,0,0)
print(result)