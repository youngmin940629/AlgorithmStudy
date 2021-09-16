'''
8
0 1 0 1 0 0 0 1
2
1 3
2 3
'''
# 스위치 개수 입력
N = int(input())
# 스위치 상태 list로 입력
data = [2] + list(map(int, input().split())) + [3]
# 사람 수 입력
stu_num = int(input())
# 리스트에 학생 정보 입력
students = [list(map(int, input().split())) for _ in range(stu_num)]

# 스위치 껐다 켜는 함수 설정
def switch(n):
    if data[n] == 0:
        data[n] = 1
    elif data[n] == 1:
        data[n] = 0

for student in students:
    # 남학생인 경우 => 숫자의 배수가 되는 인덱스의 스위치 상태 바꿈
    if student[0] == 1:
        for i in range(1, N+1):
            if i % student[1] == 0:
                switch(i)
    # 여학생인 경우 => 회문 검사해서 회문이면 그 구간의 스위치 모두 상태변경
    # 아니면 그 숫자의 스위치만 변경
    elif student[0] == 2:
        idx = student[1]
        switch(idx)
        if data[idx-1] != data[idx+1]:
            continue # 처음에 break로 했는데 안됐음 => for문 자체를 나가버리게 됨
        else:
            plus = 1
            while data[idx-plus] == data[idx+plus]:
                switch(idx-plus)
                switch(idx+plus)
                plus += 1
# 출력 경우의수...?
for i in range(1, N+1):
    print(data[i], end=' ')
    if i % 20 == 0:
        print()
