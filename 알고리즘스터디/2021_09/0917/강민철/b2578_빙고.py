bingo = [list(map(int, input().split())) for _ in range(5)]
arr = list()
for _ in range(5):
    arr.extend(map(int, input().split()))
idx = 0
while idx < 25:
    cnt = 0
    for i in range(5):
        flag = 0
        for j in range(5):
            if bingo[i][j] == arr[idx]:
                bingo[i][j] = 0
                flag = 1
                break
        if flag == 1:
            break
    if idx >= 11:
        for i in range(5):
            if sum(bingo[i]) == 0:
                cnt += 1
        for i in range(5):
            if bingo[0][i] == 0:
                col_sum = 0
                for j in range(5):
                    col_sum += bingo[j][i]
                if col_sum == 0:
                    cnt += 1
        if bingo[0][0] == 0:
            dia = 0
            for i in range(5):
                dia += bingo[i][i]
            if dia == 0:
                cnt += 1
        if bingo[0][4] == 0:
            dia = 0
            for i in range(5):
                dia += bingo[i][4-i]
            if dia == 0:
                cnt += 1
    if cnt >= 3:
        print(idx+1)
        break
    idx += 1
