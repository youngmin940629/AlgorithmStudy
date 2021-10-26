def st(i=0, s=0):
    if s == K:
        global ans
        ans += 1
    elif i < N:
        st(i+1, s)
        if s+nums[i] <= K:
            st(i+1, s+nums[i])


for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    nums = tuple(map(int, input().split()))
    ans = 0
    st()
    print('#{} {}'.format(tc, ans))