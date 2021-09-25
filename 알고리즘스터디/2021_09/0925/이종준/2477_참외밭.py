# 1m**2에서 자라는 참외의 개수 입력
K = int(input())
# 참외밭 방향 밑 이동거리
data = [list(map(int, input().split())) for _ in range(6)]

width_list = [1, 2] # 동, 서
height_list = [3, 4] # 남, 북

# dir: direction
dir_list = []

width_idx = 0
height_idx = 0

for i in data:
    dir_list.append(i[0])

for i in range(6):
    if dir_list[i] in width_list and dir_list.count(dir_list[i]) == 1:
        width_idx = i
    elif dir_list[i] in height_list and dir_list.count(dir_list[i]) == 1:
        height_idx = i

# 큰 사각형
big = data[width_idx][1] * data[height_idx][1]

# 작은 사각형
'''
0
1
2
3
4
5
인덱스가 0, 5인 경우 예외처리
'''
if min(width_idx, height_idx) == 0 and max(width_idx, height_idx) == 5:
    small = data[2][1] * data[3][1]
else:
    small = data[(min(width_idx, height_idx) + 3) % 6][1] * data[(min(width_idx, height_idx) + 4) % 6][1]

# 큰 - 작은 = 최종 밭 넓이
final = big - small

print(K * final)