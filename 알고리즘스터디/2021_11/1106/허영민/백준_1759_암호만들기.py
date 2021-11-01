L, C = map(int, input().split())
data = input().split()
data.sort()
check_word = ['a', 'e', 'i', 'o', 'u']
visit = [0] * C
def word(x, st, w, check1, check2):
    if x == L:
        if check1 >= 1 and check2 >= 2:
            print(w)
    else:
        if C - st + len(w) >= 4:
            for i in range(st,C):
                if not visit[i]:
                    if data[i] in check_word:
                        visit[i] = 1
                        word(x+1, i+1, w+data[i], check1+1, check2)
                        visit[i] = 0
                    else:
                        visit[i] = 1
                        word(x+1, i+1, w+data[i], check1, check2+1)
                        visit[i] = 0
word(0,0,'',0,0)