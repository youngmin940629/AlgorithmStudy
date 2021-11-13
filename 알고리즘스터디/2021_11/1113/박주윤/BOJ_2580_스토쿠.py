import sys; sys.stdin = open('BOJ_2580_스토쿠.txt','r')

arr = [list(map(int, input().split())) for _ in range(9)]
# 81개의 리스트 주머니를 만들어서 각 위치에 들어갈 수 있는 숫자를 넣어보고 비교하며 지워 나간다.
s = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            s.append((i, j))
for i in range(9):
    s[i].count(0)
    print(s)
    print(s[i].count(0))
print(sorted(arr[0]))
'''
열과 행의 중복된 수를 구한다.
1개인 튜플을 불러와서 열 혹은 행을 sort한 후 값을 넣어준다. 이후 arr 을 변경해주고 변경된 열과 행의 중복된 수를 구한다.
값이 중복적으로 부족할 
'''
