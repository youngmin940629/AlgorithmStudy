def check(x):
    global result
    if x == 11 and sum(position) > result:
        result = sum(position)
        return
    elif x < 11:
        for i in range(11):
            if data[x][i] != 0 and not visit[i]:
                position[x] = data[x][i]
                visit[i] = 1
                check(x+1)
                visit[i] = 0
                position[x] = 0


for tc in range(int(input())):
    data = [list(map(int, input().split())) for _ in range(11)]
    result = 0
    position = [0] * (11)
    visit = [0] * (11)
    check(0)
    print(result)