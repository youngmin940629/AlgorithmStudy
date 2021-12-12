import copy
n, m = map(int,input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
max_ = 0
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def select(s, cnt):
    global max_
    if cnt == 3:
        sel_lst = copy.deepcopy(lst)
        for r in range(n):
            for c in range(m):
                spread(r,c,sel_lst)
        safe = sum(i.count(0) for i in sel_lst)
        max_ = max(max_, safe)
        return True
    else:
        for i in range(s,n*m):
            r = i//m
            c = i%m
            if lst[r][c] == 0:
                lst[r][c] = 1
                select(i, cnt+1)
                lst[r][c] = 0
def spread(r,c,sel_lst):
    if sel_lst[r][c] == 2:
        for d in range(4):
            nr = r+dr[d]
            nc = c+dc[d]
            if n > nr >= 0 and m > nc >= 0:
                if sel_lst[nr][nc] == 0:
                    sel_lst[nr][nc] = 2
                    spread(nr, nc, sel_lst)
select(0,0)
print(max_)

