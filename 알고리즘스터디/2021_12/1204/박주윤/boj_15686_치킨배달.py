# 1들의 위치를 받은 리스트 생성하자
# 2의 위치를 받은 리스트를 생성하자
# 매니투매니 하는 것처럼 1 과 2 의 길이 관계를 테이블로 하나 만들자
# M을 생각해야 하기 때문에 행렬을 만들어서 조합값을 더한다.
# 동철이의 일분배처럼 하면 된다.
#   1 2 3 4 5
# 1 1 2 2 2 1
# 2 2 3 3 2 5
# 3 4 2 1 2 3
# 4 1 5 3 2 4
# 5 1 2 4 2 1
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
s1 = []
s2 = []
for j in range(N):
    for i in range(N):
        if arr[j][i] == 1:
            s1.append((j,i))
        elif arr[j][i] == 2:
            s2.append((j,i))
print(s1)
print(s2)
lst = [[] * len(s2)]

for i in range(len(s2)):
    way = 0
    for j in range(len(s1)):
        way = abs(s2[i][0] - s1[j][0]) + abs(s2[i][1] - s1[j][1])
        lst[i].append(way)
print(lst)