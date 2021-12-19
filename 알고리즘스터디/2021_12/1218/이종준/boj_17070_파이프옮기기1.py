N = int(input())
my_map = [list(map(int, input().split())) for _ in range(N)]
# 가로 세로 대각선 => 0, 1, 2로 3차원 배열을 만들기
dp = [[[0] * N for _ in range(N)] for _ in range(3)]

# 맨 처음 위치
dp[0][0][1] = 1

# 처음에 가로부분만 진행
for i in range(2, N):
    if my_map[0][i] == 0:
        dp[0][0][i] = dp[0][0][i - 1]

for i in range(1, N):
    for j in range(2, N):
        # 대각선 진행하기
        if not my_map[i][j] and not my_map[i-1][j] and not my_map[i][j-1]:
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]
        if not my_map[i][j]:
            # 가로 진행하기
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
            # 세로 진행하기
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]

# 정답 출력할 변수 ans
ans = 0
for i in range(3):
    ans += dp[i][N-1][N-1]
print(ans)