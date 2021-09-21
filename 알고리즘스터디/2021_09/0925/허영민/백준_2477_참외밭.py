K = int(input())
data = []
cnt_arr = [0] * 5
width = 0
height = 0
sm_wid = 0
sm_hei = 0
for i in range(6):
    data.append(list(map(int, input().split())))
for idx in data:
    cnt_arr[idx[0]] += 1
cnt = 0
for road in data:
    if cnt_arr[road[0]] == 1:
        if road[0] == 4 or road[0] == 3:
            height = road[1]
        else:
            width = road[1]
for idx in range(6):
    check = data[(idx + 1)%6][1] + data[(idx - 1)%6][1]
    if check == width or check == height:
        if data[idx][0] == 4 or data[idx][0] == 3:
            sm_hei = data[idx][1]
        else:
            sm_wid = data[idx][1]
total = (width * height) - (sm_wid * sm_hei)
print(K * total)