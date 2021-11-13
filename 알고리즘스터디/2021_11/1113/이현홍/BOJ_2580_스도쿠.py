# 빈칸 첫번째부터 전부 채운다는 개념으로 인덱스 0부터 끝까지 
def sudoku(n=0):
    global ans
    if ans != -1:
        return
    if n == len(zero):
        ans = [arr[i][:] for i in range(9)]
        return
    
    r, c = zero[n]
    # 사용 번호 체크용 1: 미사용, 0: 사용
    nums[n] = [1] * 10

    # 구역 확인
    sr = 3 * (r//3)
    sc = 3 * (c//3)
    for br in range(sr, sr+3):
        for bc in range(sc, sc+3):
            if arr[br][bc]: nums[n][arr[br][bc]] = 0
    
    # 가로 확인
    for x in range(9):
        if arr[r][x]: nums[n][arr[r][x]] = 0
    
    # 세로 확인
    for y in range(9):
        if arr[y][c]: nums[n][arr[y][c]] = 0
    
    # 미사용된 번호 사용하며 완전탐색
    for i in range(1,10):
        if nums[n][i]:
            arr[r][c] = i
            sudoku(n+1)
            arr[r][c] = 0

arr = [list(map(int, input().split())) for _ in range(9)]
ans = -1

# 빈칸 전부 리스트에 담기
zero = []
for r in range(9):
    for c in range(9):
        if arr[r][c] == 0:
            zero.append((r, c))
nums = [[0] for _ in range(len(zero))]
sudoku()

for a in ans:
    print(" ".join(map(str, a)))