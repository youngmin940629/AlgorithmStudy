arr = []

# 맨 밑의 0이 나올 때까지 arr에 저장
while True:
    tmp_list = list(map(int, input().split()))
    if tmp_list == [0]:
        break
    else:
        arr.append(tmp_list)

def comb(k, s):
    if k == 6:
        print(' '.join(map(str, pick)))
        return
    
    for i in range(s, N):
        pick.append(lotto_list[i])
        comb(k + 1, i + 1)
        pick.pop()


for i in range(len(arr)):
    lotto_list = arr[i]
    N = lotto_list.pop(0)
    pick = []
    comb(0, 0)
    print()