t = int(input())
road = list(map(int, input().split()))

h = 0
tmp_h = 0

for i in range(1, t):
    if road[i-1] < road[i]:
        tmp_h = tmp_h + road[i] - road[i-1]
        if i == t-1 and tmp_h > h:
            h = tmp_h
    elif road[i - 1] >= road[i]:
        if tmp_h > h:
            h = tmp_h
            tmp_h = 0
        else: tmp_h = 0

print(h)