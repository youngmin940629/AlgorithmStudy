def check(x,y,num):
    for i in range(9):
        if sudoku[x][i] == num or sudoku[i][y] == num:
            return False
    check_x = x // 3
    check_y = y // 3
    for nx in range(3):
        for ny in range(3):
            if sudoku[(check_x * 3) + nx][(check_y * 3) + ny] == num:
                return False
    return True

def sol_sudoku(idx):
    if idx == check_cnt:
        return
    else:
        x,y = check_list[idx]
        for number in range(1,10):
            if sudoku[x][y] == 0:
                if check(x,y,number):
                    sudoku[x][y] = number
                    sol_sudoku(idx+1)
        if sudoku[x][y] == 0:
            x,y = check_list[idx-1]
            sudoku[x][y] = 0


sudoku = [list(map(int, input().split())) for _ in range(9)]
check_list = []
for x in range(9):
    for y in range(9):
        if sudoku[x][y] == 0:
            check_list.append((x,y))
check_cnt = len(check_list)
sol_sudoku(0)
for i in range(9):
    print(' '.join(map(str, sudoku[i])))