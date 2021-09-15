bingo = [list(map(int, input().split())) for _ in range(5)]
call = []
check = 0
for _ in range(5):
    a, b, c, d, e = map(int, input().split())
    call += [a] + [b] + [c] + [d] + [e]
for cnt in range(25):
    for y in range(5):
        for x in range(5):
            if call[cnt] == bingo[y][x]:
                bingo[y][x] = 0
    if cnt >= 11:
        check = 0
        for num in range(5):
            check_cnt = 0
            if bingo[num][0] == 0:
                for idx in range(5):
                    check_cnt += bingo[num][idx]
                if check_cnt == 0:
                    check += 1

            if bingo[0][num] == 0:
                check_cnt = 0
                if bingo[0][num] == 0:
                    for idx in range(5):
                        check_cnt += bingo[idx][num]
                    if check_cnt == 0:
                        check += 1

        if bingo[0][0] == 0:
            check_cnt = 0
            for idx in range(5):
                check_cnt += bingo[idx][idx]
            if check_cnt == 0:
                check += 1

        if bingo[0][4] == 0:
            check_cnt = 0
            for idx in range(5):
                check_cnt += bingo[idx][4-idx]
            if check_cnt == 0:
                check += 1
    if check >= 3:
        break
print(cnt+1)