def st(i=0, s=0):
    if s == K:          # K가 나오면 ans + 1
        global ans
        ans += 1
    elif i < N:
        st(i+1, s)      # 더하지 않는 경우 무조건 진행
        if s+nums[i] <= K:
            st(i+1, s+nums[i])  # K보다 작으면 더한 것도 진행


for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    nums = tuple(map(int, input().split()))
    ans = 0
    st()
    print('#{} {}'.format(tc, ans))