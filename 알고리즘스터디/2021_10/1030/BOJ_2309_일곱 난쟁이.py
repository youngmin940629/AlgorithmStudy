s = 0
H = [0] * 9
for i in range(9):
    H[i] = int(input())
    s += H[i]
H.sort()            # 9명 받아서 미리 정렬

t = s - 100         # 제거대상의 합
B = 0
for i in range(8):
    for j in range(i+1, 9):
        if H[i] + H[j] == t:        # 가짜 2명이 100을 깨뜨리는 놈
            H[i], H[j], B = -1, -1, 1   # 잡으면 종료
            break
    if B: break

for h in H:
    if h > 0: print(h)      # -1을 건너뛰고 출력