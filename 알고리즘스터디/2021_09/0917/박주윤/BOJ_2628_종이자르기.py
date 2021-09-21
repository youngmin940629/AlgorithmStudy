import sys; sys.stdin = open('BOJ_2628_종이자르기.txt','r')


N, M = map(int, input().split())
lst_0 = []
lst_1 = []
lst1 = []
lst2 = []
max_ = 0
for _ in range(int(input())):
    n, m = map(int, input().split())
    if n == 0:
        lst_0.append(m)
    else:
        lst_1.append(m)
s_0 = [0] + sorted(lst_0) + [M]
s_1 = [0] + sorted(lst_1) + [N]

for i in range(len(s_0)-1):
    lst1.append(s_0[i+1]-s_0[i])
for j in range(len(s_1)-1):
    lst2.append(s_1[j+1]-s_1[j])
for i in range(len(lst1)):
    for j in range(len(lst2)):
        if max_ < lst1[i]*lst2[j]:
            max_ = lst1[i]*lst2[j]
print(max_)