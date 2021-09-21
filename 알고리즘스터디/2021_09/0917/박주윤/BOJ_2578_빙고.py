import sys; sys.stdin = open('BOJ_2578_빙고.txt', 'r')
lst_r = []
lst_s = []
idx = []
lst = [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24],[4,8,12,16,20],[0,6,12,18,24],[0,5,10,15,20],[1,6,11,16,21],[2,7,12,17,22],[3,8,13,18,23],[4,9,14,19,24]]
cnt = 0
ans = []
last = []
for _ in range(5):
    lst_r += map(int, input().split())
for _ in range(5):
    lst_s += map(int, input().split())

for j in range(25):
    for i in range(25):
        if lst_r[i] == lst_s[j]:
            idx.append(i)
            cnt += 1
            if cnt >= 12:
                for k in range(12):
                    if lst[k][0] in idx and lst[k][1] in idx and lst[k][2] in idx and lst[k][3] in idx and lst[k][4] in idx:
                        ans.append(k)
                        if len(set(ans)) == 3:
                            last.append(cnt)
print(last[0])