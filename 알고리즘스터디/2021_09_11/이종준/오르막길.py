'''
5
1 2 1 4 6
'''
N = int(input())
data = list(map(int, input().split())) + [1]

start = data[0]
max_height = 0
for i in range(N):
    if data[i] >= data[i + 1]:
        road_height = data[i] - start
        start = data[i + 1]
        if max_height < road_height:
            max_height = road_height
if max_height == 0:
    print(0)
else:
    print(max_height)