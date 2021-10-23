import sys; sys.stdin=open('BOJ_15649_N,M.txt','r')

n, m = map(int,input().split()) # 입력받아주고
visited = [0] * n               # visit 를 만들어 준다
lst = []                        # 출력을 위한 빈 리스트 생성
def dfs(d):                     # 깊이 우선 탐색
    if d == m:                  # 출력조건
        print(' '.join(map(str, lst)))
        return
    for i in range(n):          # 원하는 값 만큼
        if not visited[i]:      # 방문하지 않은 경우
            visited[i] = 1      # 방문 표시 하고
            lst.append(i+1)     # 그 값을 lst에 넣어주고
            dfs(d+1)            # 재귀를 통해 d == m 이 될때까지 반복해 준다.
            visited[i] = 0      # 돌아와서 다시 지워주고
            lst.pop()           #
dfs(0)

#