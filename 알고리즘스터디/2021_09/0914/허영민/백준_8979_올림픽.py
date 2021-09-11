N, K = map(int, input().split())
score = list([] for _ in range(N+1))
cnt = 1
for nation in range(N):
    nation, gold, silver, bronze = map(int, input().split())
    score[nation] = [gold, silver, bronze]
gold_K, silver_K, bronze_K = score[K][0], score[K][1], score[K][2]
for nation in range(1, N+1):
    if score[nation][0] > gold_K:
        cnt += 1
    elif score[nation][0] == gold_K:
        if score[nation][1] > silver_K:
            cnt += 1
        elif score[nation][1] == silver_K:
            if score[nation][2] > bronze_K:
                cnt += 1
print(cnt)