## 정답 예시 (이날 안풀었음)

sudoku = [] #스도쿠 판을 입력받을 리스트
print("스도쿠판을 입력해주세요.\n")

for i in range(9):
    a = list(map(int, input().split())) 
    # map함수를 통해, 입력받은 값을 공백' '을 기준으로 쪼개고, 정수형으로 리스트 a에 저장
    sudoku.append(a) # 저장된 a리스트를 리스트 sudoku에 추가

result = True # 스도쿠의 결과

for i in range(3): # 각 3x3크기의 칸을 비교할 반복문
    idx1 = 0 # 세로 위치를 나타낼 인덱스
    for j in range(3):
        idx2 = 0 # 가로 위치를 나타낼 인덱스
        lst = [] # 3x3칸에 존재하는 숫자를 임시 저장할 리스트

        for k in range(idx1, idx1+3): # 가로 3칸
            for l in range(idx2, idx2+3): # 세로 3칸
                lst.append(sudoku[l][k]) # 각 칸에 존재하는 요소를 lst에 저장
        
        lst = list(set(lst)) # 집합 자료형을 이용하여 중복된 요소 제거
        if len(lst) == 9: # 제거된 숫자가 없을 경우
            idx1 += 3 # 다음 칸으로 이동(가로)
        else:
            result = False # 만약 제거된 요소가 있다면, 중복되는 숫자가 있으므로 오답
            break
    idx2 += 3 # 다음 칸으로 이동(세로)

# 가로 줄 비교
for i in range(9): 
    if len(list(set(sudoku[i])))!=9: # 한 줄에 중복되는 숫자가 있는지 집합 자료형을 이용하여 제거
        result = False # 만약 제거된 요소가 있다면, 중복되는 숫자가 있으므로 오답
        break

# 세로 줄 비교
for i in range(9): 
    lst = [] # 각 세로 줄의 요소를 임시 저장할 리스트
    for j in range(9):
        lst.append(sudoku[j][i]) # 세로 한 줄의 요소 lst에 저장
    if len(list(set(lst))) != 9: # 한 줄에 중복되는 숫자가 있는지 집합 자료형을 이용하여 제거
        result = False # 만약 제거된 요소가 있다면, 중복되는 숫자가 있으므로 오답
        break

if result: # 결과에 따른 출력
    print("\n입력하신 스도쿠는 정답입니다.")
else:
    print("\n입력하신 스도쿠는 오답입니다.")