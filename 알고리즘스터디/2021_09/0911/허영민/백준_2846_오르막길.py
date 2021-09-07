N = int(input())
data = list(map(int, input().split()))
road = []
result = 0
for idx in range(N-1, -1, -1):
    if idx > 0 and data[idx] > data[idx-1]:
        road.append(data[idx])
    elif idx == 0:
        road.append(data[idx])
        if len(road) > 1:
            tmp_result = road[0] - road[-1]
            if result < tmp_result:
                result = tmp_result
    elif data[idx] <= data[idx-1]:
        road.append(data[idx])
        if len(road) > 1:
            tmp_result = road[0] - road[-1]
            if result < tmp_result:
                result = tmp_result
            road = []
        else:
            road = []
print(result)