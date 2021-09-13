'''
4 3
1 1 2 0
2 0 1 0
3 0 1 0
4 0 0 1
'''

N, K = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
ranking = 1
country_idx = 0
for i in range(N):
    if data[i][0] == K:
        country_idx = i
for i in range(N):
    if data[i][1] > data[country_idx][1]:
        ranking += 1
    elif data[i][1] == data[country_idx][1]:
        if data[i][2] > data[country_idx][2]:
            ranking += 1
        elif data[i][2] == data[country_idx][2]:
            if data[i][3] > data[country_idx][3]:
                ranking += 1
print(ranking)