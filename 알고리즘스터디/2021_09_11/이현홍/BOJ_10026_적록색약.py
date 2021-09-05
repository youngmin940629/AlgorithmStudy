# 재귀함수 깊이 런타임 에러 처리
import sys
sys.setrecursionlimit(10**6)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

N = int(input())
arr1 = [0] * N
arr2 = [[0] * N for _ in range(N)]

# 너비 우선 탐색 → 들어온 값과 같을 시 같은 값으로 입력 되게 만듦
def BFS(arr, N, y, x, c, n):
# arr 배열(1일반, 2색약), N 길이, y,x, c(컬러 코드 -1,-2,(-3)), n 구역
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0<= nx < N and arr[ny][nx] == c:
            arr[ny][nx] = n
            BFS(arr, N, ny, nx, c, n)

# 배열 하나 만들고
for n in range(N):
    arr1[n] = (":".join(input())).split(":")

# 색약인 경우 배열2로 구분 시킴
for r in range(N):
    for c in range(N):
        if arr1[r][c] == 'R':
            arr2[r][c] = -1
            arr1[r][c] = -1
        elif arr1[r][c] == 'G':
            arr2[r][c] = -1
            arr1[r][c] = -2
        elif arr1[r][c] == 'B':
            arr2[r][c] = -2
            arr1[r][c] = -3

# 함수의 최초 호출 때 n값이 +1됨(n값 = 구역 num)
n1 = n2 = 0
for y in range(N):
    for x in range(N):
        if arr1[y][x] == -1 or arr1[y][x] == -2 or arr1[y][x] == -3:
            n1 += 1
            BFS(arr1, N, y, x, arr1[y][x], n1)
        
        if arr2[y][x] == -1 or arr2[y][x] == -2:
            n2 += 1
            BFS(arr2, N, y, x, arr2[y][x], n2)

print(n1, n2)