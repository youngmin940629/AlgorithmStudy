N = int(input())
players = []
data = {}
result = []
for _ in range(N):
    player = input()
    players.append(player)
for i in range(N):
    data[players[i][0]] = 0
for idx in range(N):
    data[players[idx][0]] += 1
for key in data:
    if data[key] >= 5:
        result.append(key)
else:
    if result:
        result.sort()
        print(''.join(map(str, result)))
    else:
        print('PREDAJA')