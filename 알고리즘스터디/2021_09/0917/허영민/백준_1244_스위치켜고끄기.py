sw = int(input())
switch = list(map(int, input().split()))
sw_cnt = [0] * (sw+1)
for idx in range(sw):
    if switch[idx] == 1:
        sw_cnt[idx+1] = 1
N = int(input())
for _ in range(N):
    student = list(map(int, input().split()))
    if student[0] == 1:
        sw_check = student[1]
        while sw_check <= sw:
            if sw_cnt[sw_check]:
                sw_cnt[sw_check] = 0
            else:
                sw_cnt[sw_check] = 1
            sw_check += student[1]
    elif student[0] == 2:
        cnt = 1
        if sw_cnt[student[1]]:
            sw_cnt[student[1]] = 0
        else:
            sw_cnt[student[1]] = 1
        while ((student[1] - cnt) > 0) and ((student[1] + cnt) <= sw):
            if sw_cnt[student[1] - cnt] != sw_cnt[student[1] + cnt]:
                break
            else:
                cnt += 1
        for i in range(1, cnt):
            if sw_cnt[student[1] - i]:
                sw_cnt[student[1] - i] = sw_cnt[student[1] + i] = 0
            else:
                sw_cnt[student[1] - i] = sw_cnt[student[1] + i] = 1
for idx in range(1, sw+1):
    if idx % 20 == 0:
        print('{}'.format(sw_cnt[idx]))
    else:
        print('{} '.format(sw_cnt[idx]), end='')