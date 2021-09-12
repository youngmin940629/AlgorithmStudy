import sys; sys.stdin = open('BOJ_2804_크로스워드 만들기.txt', 'r')

for tc in range(1, int(input())+1):
    tc_num = int(input())
    a, b = map(str, input().split())
    N = len(a)
    M = len(b)
    ilist = []
    jlist = []
    lst = [[0] * N for _ in range(M)]

    for i in range(N):
        for j in range(M):
            if a[i] == b[j]:
                ilist.append(i)
                jlist.append(j)


    i_idx = ilist[0]
    j_idx = jlist[0]

    for i in range(M):
        lst[i][i_idx] = b[i]
    for j in range(N):
        lst[j_idx][j] = a[j]
    for i in range(M):
        for j in range(N):
            if lst[i][j] == 0:
                lst[i][j] = '.'

    for i in range(M):
        for j in range(N):
            print(lst[i][j], end = '')
        print()


