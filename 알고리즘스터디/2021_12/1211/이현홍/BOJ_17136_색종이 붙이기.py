import sys
sys.stdin = open('sample.txt', 'r')

paper = {0:5, 1:5, 2:5, 3:5, 4:5}

arr = [list(map(int, input().split())) for _ in range(10)]
result = -1

# 색종이 덮기
def cover(r, c, k):
    for i in range(k+1):
        for j in range(k+1):
            arr[r+i][c+j] = 0

# 색종이 빼기
def recover(r, c, k):
    for i in range(k+1):
        for j in range(k+1):
            arr[r+i][c+j] = 1

# 완전 탐색
def sc(s=0):
    global result
    if result != -1 and result <= s: return            # 종이 더 들면 리턴
    for r in range(10):
        for c in range(10):
            if arr[r][c] == 1:                        # 1 만나면
                for k in range(4, -1, -1):            # 큰 종이부터 집어 넣어봄
                    if 0 < paper[k] and r+k < 10 and c+k < 10:
                        if arr[r+k][c] and arr[r][c+k] and arr[r+k][c+k]:
                            x = 1
                            for i in range(k+1):            # 정사각형 체크
                                for j in range(k+1):
                                    if arr[r+i][c+j] == 0:
                                        x = 0
                            if x:
                                paper[k] -= 1
                                cover(r, c, k)          # 종이 덮고 다음 진행
                                sc(s+1)                 # 0, 0부터 탐색하는 비효율 발생하지만 배열 작아서 상관x
                                paper[k] += 1
                                recover(r, c, k)        # 종이 빼기
                return                                  # 1을 만났으면 무조건 여기서 끝
    if result == -1 or s < result:                      # 0밖에 안 남았을 때
        result = s
sc()
print(result)