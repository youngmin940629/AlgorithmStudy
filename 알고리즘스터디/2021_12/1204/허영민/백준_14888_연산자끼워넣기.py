N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))
max_result = -1000000001
min_result = 1000000001
def computing(cnt, rst, plus, subtract, multiple, division):
    global max_result, min_result
    if cnt == N:
        max_result = max(rst,max_result)
        min_result = min(rst,min_result)
        return
    else:
        if plus:
            computing(cnt+1, rst+numbers[cnt], plus-1, subtract, multiple, division)
        if subtract:
            computing(cnt + 1, rst - numbers[cnt], plus, subtract-1, multiple, division)
        if multiple:
            computing(cnt + 1, rst * numbers[cnt], plus, subtract, multiple-1, division)
        if division:
            if rst < 0:
                computing(cnt+1, -(-rst // numbers[cnt]), plus, subtract, multiple, division-1)
            elif rst >= 0:
                computing(cnt + 1, rst // numbers[cnt], plus, subtract, multiple, division-1)
computing(1, numbers[0], operators[0], operators[1], operators[2], operators[3])
print(max_result, min_result)