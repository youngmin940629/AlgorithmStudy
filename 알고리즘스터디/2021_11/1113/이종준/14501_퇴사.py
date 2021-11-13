# DP를 이용해야 할듯?

N = int(input())

data = []

for _ in range(N):
    data.append(list(map(int, input().split())))

dp_list = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    # 최대 일수 넘어가면 패스
    if data[i][0] + i > N:
        dp_list[i] = dp_list[i + 1]
    # 현재 일에서의 보상 + 다음날까지 누적 보상 vs 일 안 맡을 경우의 보상
    else:
        dp_list[i] = max(data[i][1] + dp_list[i + data[i][0]], dp_list[i + 1])

print(dp_list[0])