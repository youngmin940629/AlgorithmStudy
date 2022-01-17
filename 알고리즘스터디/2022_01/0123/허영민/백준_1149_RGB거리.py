N = int(input())
home_color = []
for _ in range(N):
    home_color.append(list(map(int, input().split())))
result = [[home_color[0][0], home_color[0][1], home_color[0][2]] for _ in range(N)]
for i in range(1,N):
    result[i][0] = home_color[i][0] + min(result[i-1][1], result[i-1][2])
    result[i][1] = home_color[i][1] + min(result[i-1][0], result[i-1][2])
    result[i][2] = home_color[i][2] + min(result[i-1][0], result[i-1][1])
print(min(result[N-1]))