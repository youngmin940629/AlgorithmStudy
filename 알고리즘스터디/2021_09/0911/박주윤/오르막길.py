import sys; sys.stdin = open('2864.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    s = []
    t = []
    ans2 = max_ = 0
    for i in range(N-1):
        ans = arr[i]-arr[i+1]
        t.append(ans)
    for i in range(len(t)):
        if t[i] < 0:
            s.append(t[i])
            if i == len(t)-1:
                while s:
                    ans2 += s.pop()
                if max_ > ans2:
                    max_ = ans2
        elif s != [] and t[i] >= 0:
            while s:
                ans2 += s.pop()
            if max_ > ans2:
                max_ = ans2
            ans2 = 0
    print(abs(max_))



    # 스택을 쓰고 싶어 스택은 [[0]*N for _ in range(N)]
    # 먼저 1 과 2 의 차이를 전부 리스트에 담고
    # 스택에 연속된 음수의 합을 구해
    # 0 이나 양수가 나오면 다음 스택에 담아
    # 스택내의 값의 크기중 최댓값을 구해야지