# 정신나간 상근이 문제
alp = []
t = int(input())
for i in range(t):
    name = input()
    alp.append(name[0])     # 앞글자만 추출

first = sorted(list(set(alp)))      # 정렬된 중복 제거 list
result = ''

for j in first:
    if alp.count(j) >= 5:       # 생성 리스트 값이 처음 추출 리스트에 몇 개인지 추출, 5개 이상이면 추가
        result += j

if result == '':
    result = 'PREDAJA'
print(result)