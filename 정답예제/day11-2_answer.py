## 정답 예시

def rsp_num_name(a): # 각 숫자에 대해 '가위', '바위', '보' 값을 반환하는 함수
    if a == 1: # 가위는 숫자 1에 대응
        return "가위" 
    elif a == 2: # 바위는 숫자 2에 대응
        return "바위"
    else: # 보는 숫자 3에 대응(난수 범위가 1~3이기 때문에 남은 숫자가 3)
        return "보"

def rsp_name_num(rsp):# 각 '가위, 바위, 보' 문자열 값에 숫자를 대응시키는 함수
    if rsp == "가위":
        return 1
    elif rsp == "바위":
        return 2
    else:
        return 3

def rsp_winner(a, b): # 가위바위보의 결과를 
    return a-b

import random # 랜덤 모듈 import

n = random.randint(1, 3) # 1부터 3 사이의 정수 중에서 난수 값 반환
you = input("가위바위보 게임입니다. 무엇을 낼 지 입력해주세요: ") # 입력 받기
print("당신  :", you) 
print("컴퓨터:", rsp_num_name(n)) # 함수 사용
w = rsp_winner(rsp_name_num(you),n) # w에 게임 결과 저장
if w == 0:
    print("비겼습니다.")
elif w==1 or -2:  
    print("축하합니다. 당신이 이겼습니다.")
		# 숫자 차이가 1또는 -2일때 이김
		# 예를 들어 입력이 '가위'이면 그에 해당하는 숫자는 1임
		# 그 상황에서 컴퓨터 값이 '보'이면 숫자 3을 가리키고, w값은 1 - 3 = -2가 됨
else:
    print("당신이 졌습니다.")