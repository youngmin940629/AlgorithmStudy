num, what_rank = map(int, input().split())

nations = []
for i in range(num):
    nations.append(list(map(int, input().split())))

# 국가 id num을 뒤로 옮김
for nation in nations:
    tmp = nation.pop(0)
    nation.append(tmp)

# 금 은 동 id가 오름차순으로 정렬 후 reverse
nations.sort()
nations.reverse()

for i in range(len(nations)):
    # 앞에서부터 index + 1등
    if i == 0:
        nations[i].append(i+1)
    # 메달 수가 전부 같다면 이전 등수와 동등
    elif nations[i][0] == nations[i-1][0] and nations[i][1] == nations[i-1][1] and nations[i][2] == nations[i-1][2]:
        nations[i].append(nations[i - 1][-1])
    else:
        nations[i].append(i+1)

# id가 주어진 정수면, 등수 출력
for nation in nations:
    if nation[-2] == what_rank:
        print(nation[-1])