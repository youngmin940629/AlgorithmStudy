dwarfs = []

# 한 줄씩 입력되므로 이런 식으로 리스트에 append함
for _ in range(9):
    dwarf = int(input())
    dwarfs.append(dwarf)

# 일곱명을 뽑아서 저장할 리스트 pick
pick = []


def find_seven(k, s):
    # 일곱 명을 다 뽑았을 때
    if k == 7:
        # 합이 100인 경우 정렬해서 한 줄에 하나씩 출력
        if sum(pick) == 100:
            pick.sort()
            for i in range(7):
                print(pick[i])
        return
    
    # 일곱 개를 뽑는 logic
    for i in range(s, 9):
        pick.append(dwarfs[i])
        find_seven(k + 1, i + 1)
        pick.pop()

# 함수 실행
find_seven(0, 0)