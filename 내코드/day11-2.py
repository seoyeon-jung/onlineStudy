# 난이도 상 : **가위바위보 게임**
    
# 아래의 조건에 따라 컴퓨터와 가위바위보 게임을 할 수 있는 간단한 게임을 만들어보세요.
    
# 조건 1 : random 모듈을 사용하여 만들어주세요.
# random 모듈 간단하게 알아보기
#   - 파이썬에서 제공하는 난수 활용 모듈
#   - random.random() :  0이상 1미만 사이의 실수로 난수를 구함
#   - random.ranint(a, b) : a이상 b이하 사이의 정수로 난수를 구함
# 조건 2 : 프로그램에서 '가위', '바위', '보' 중 하나를 입력하면 게임을 진행합니다. 다른 입력 사항은 고려하지 않습니다.
# 조건 3 : 함수를 최소 2개 이상은 사용하여 만들어주세요
# 조건 4:  게임 결과(이김, 비김, 짐)에 따른 출력을 해주세요.

import random

while True:
    game = input("가위바위보 게임입니다. 무엇을 낼 지 입력해주세요: ")
    if game == '가위':
        if random.choice(["가위", "바위", "보"]) == "가위":
            print("당신: 가위")
            print("컴퓨터: 가위")
            print("비겼습니다.")
        elif random.choice(["가위", "바위", "보"]) == "바위":
            print("당신: 가위")
            print("컴퓨터: 바위")
            print("당신이 졌습니다.")
        else:
            print("당신: 가위")
            print("컴퓨터: 보")
            print("축하합니다. 당신이 이겼습니다.")
    if game == '바위':
        if random.choice(["가위", "바위", "보"]) == "가위":
            print("당신: 바위")
            print("컴퓨터: 가위")
            print("축하합니다. 당신이 이겼습니다.")
        elif random.choice(["가위", "바위", "보"]) == "바위":
            print("당신: 바위")
            print("컴퓨터: 바위")
            print("비겼습니다.")
        else:
            print("당신: 바위")
            print("컴퓨터: 보")
            print("당신이 졌습니다.")
    if game == "보":
        if random.choice(["가위", "바위", "보"]) == "가위":
            print("당신: 보")
            print("컴퓨터: 가위")
            print("당신이 졌습니다.")
        elif random.choice(["가위", "바위", "보"]) == "바위":
            print("당신: 보")
            print("컴퓨터: 바위")
            print("축하합니다. 당신이 이겼습니다.")
        else:
            print("당신: 보")
            print("컴퓨터: 보")
            print("비겼습니다.")