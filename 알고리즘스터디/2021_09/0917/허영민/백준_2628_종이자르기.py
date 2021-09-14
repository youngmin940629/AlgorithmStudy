square = list(map(int, input().split()))
N = int(input())
data = [[] for _ in range(2)]
for _ in range(N):
    a, b = map(int, input().split())
    data[a].append(b)
width_cnt = [0] * (square[0] + 1)
height_cnt = [0] * (square[1] + 1)
width = []
height = []
width_cnt[0] = width_cnt[-1] = height_cnt[0] = height_cnt[-1] = 1
for idx in data[1]:
    width_cnt[idx] = 1
for idx in data[0]:
    height_cnt[idx] = 1
for case in range(2):
    st_idx = 0
    if case == 0:
        for idx in range(len(width_cnt)):
            if width_cnt[idx] == 1:
                width.append(idx-st_idx)
                st_idx = idx
    elif case == 1:
        for idx in range(len(height_cnt)):
            if height_cnt[idx] == 1:
                height.append(idx-st_idx)
                st_idx = idx
print(max(width)*max(height))