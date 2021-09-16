'''
10 8
3
0 3
1 4
0 2
'''
# N: 가로 길이, M: 세로 길이
N, M = map(int, input().split())
# 자르는 횟수
K = int(input())
# 자르는 방향에 대한 정보
data = [list(map(int, input().split())) for _ in range(K)]
# 0: 세로 자르기
zero = [0, M]
# 1: 가로 자르기
one = [0, N]
# 각각 가로, 세로에 append하기
for cut in data:
    if cut[0] == 0:
        zero.append(cut[1])
    elif cut[0] == 1:
        one.append(cut[1])

# 리스트 정렬
zero.sort()
one.sort()
# 최대 사각형 넓이 저장할 변수 설정
max_rectangle = 0
# 각 리스트에서 길이 구해서 곱해주기
for i in range(1, len(zero)):
    for j in range(1, len(one)):
        height = zero[i] - zero[i - 1]
        width = one[j] - one[j - 1]
        my_rectangle = height * width
        # 최대 사각형 넓이 찾아서 저장
        if max_rectangle < my_rectangle:
            max_rectangle = my_rectangle
# 출력
print(max_rectangle)