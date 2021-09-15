N = int(input())
switch = list(map(int, input().split()))
tc = int(input())

# 남학생일 때
def boy(lst, n):
    for i in range(n-1, len(lst), n):
        lst[i] = (lst[i] + 1) % 2

# 여학생일 때
def girl(lst, n):
    lst[n] = (lst[n] + 1) % 2
    for i in range(1, len(lst)):
        if 0 <= n-i and n+i < len(lst):
            if lst[n+i] == lst[n-i]:
                lst[n+i] = lst[n-i] = (lst[n+i]+1) % 2
            else: break
        else: break

# 작업수행
for t in range(tc):
    s, n = map(int, input().split())
    if s == 1: boy(switch, n)
    else: girl(switch, n-1)

# 출력 조건
while len(switch) > 20:
    print(" ".join(list(map(str, switch[:20]))))
    switch = switch[20:]
print(" ".join(list(map(str, switch[:20]))))