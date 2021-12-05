# 순열 위해 permutations 사용해봄
from itertools import permutations

# 입력받기
N = int(input())
num_list = list(map(int, input().split()))
cal_list = list(map(int, input().split()))

# 기호를 저장하기 위한 빈 리스트 cals
cals = []

# + - * // 순서
# cal_list의 개수대로 기호를 cals에 저장
for i in range(4):
    if i == 0:
        for _ in range(cal_list[i]):
            cals.append('+')
    elif i == 1:
        for _ in range(cal_list[i]):
            cals.append('-')
    elif i == 2:
        for _ in range(cal_list[i]):
            cals.append('*')
    else:
        for _ in range(cal_list[i]):
            cals.append('//')

# 정답 출력할 최대, 최소값
min_cal = 123456789
max_cal = -123456789

# 순열 돌면서
for cal_tuple in set(permutations(cals, N - 1)):
    # 계산!
    tmp = num_list[0]
    for i in range(N - 1):
        if cal_tuple[i] == '+':
            tmp += num_list[i + 1]
        elif cal_tuple[i] == '-':
            tmp -= num_list[i + 1]
        elif cal_tuple[i] == '*':
            tmp *= num_list[i + 1]
        elif cal_tuple[i] == '//':
            tmp = int(tmp / num_list[i + 1])
    if min_cal > tmp:
        min_cal = tmp
    if max_cal < tmp:
        max_cal = tmp

# 정답 출력
print(max_cal)
print(min_cal)