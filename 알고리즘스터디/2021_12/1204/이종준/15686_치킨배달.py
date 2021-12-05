# 조합에서 combination을 사용해 봄
from itertools import combinations

# 입력 부분
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

# 집과 치킨집을 모두 튜플 형태로 각각 빈 리스트에 저장
houses = []
chickens = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chickens.append((i, j))
        elif city[i][j] == 1:
            houses.append((i, j))

# 답(최소 거리의 합)을 저장할 변수
min_dist = 1234567890

# 조합을 돌면서
for chicken_tuple in combinations(chickens, M):
    tmp = 0
    for house in houses:
        # 각 집마다 치킨 거리의 최소값을 tmp라는 임시 변수에 더해간다
        tmp_list = []
        for chicken in chicken_tuple:            
            tmp_list.append(abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]))
        tmp += min(tmp_list)
    # 최소값을 min_dist에 저장하면서 최신화
    if min_dist > tmp:
        min_dist = tmp

# 출력
print(min_dist)