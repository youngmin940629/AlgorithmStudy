N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
chicken = []
home = []
comb = []
for x in range(N):
    for y in range(N):
        if city[x][y] == 2:
            chicken.append((x,y))
        elif city[x][y] == 1:
            home.append((x,y))
def select(arr,n):
    tmp = arr[:]
    if len(arr) == M:
        comb.append(tmp)
        return
    else:
        for i in range(n, len(chicken)):
            tmp.append(chicken[i])
            select(tmp, i+1)
            tmp.pop()
select([],0)
result = []
for chickenShop in comb:
    chick_tmp = 0
    for hx, hy in home:
        distance = []
        for cx, cy in chickenShop:
            tmp = abs(hx-cx) + abs(hy-cy)
            distance.append(tmp)
        chick_tmp += min(distance)
    result.append(chick_tmp)
print(min(result))