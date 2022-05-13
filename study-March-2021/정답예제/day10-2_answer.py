## 정답 예시
print("1. 10초    2. 30초    3. 1분    4. 10분    5. 시작")

time = 0
while True: # 반복문
    menu = int(input("원하는 시간의 숫자 버튼을 입력해주세요 : "))
    if(menu == 1): # 각 시간 초 단위로 저장
        time += 10
    elif(menu == 2):
        time += 30
    elif(menu == 3):
        time += 60
    elif(menu == 4):
        time += 600
    elif(menu == 5): # 이외의 숫자를 입력하면 반복문 종료
        print("\n전자레인지를 작동합니다.") 
        break 
    else: # 이외의 숫자를 입력하면 반복문 종료
        print("잘못된 입력입니다.") 
        

    sec = time # sec에 time만큼의 시간 저장
    if sec >= 60: # sec가 60초 이상일 경우
        min = sec // 60 # min는 분 단위 시간이므로, sec를 60초로 나눈 몫
        sec -= min*60 # sec에서 min * 60초 만큼 뺄셈
        print(min, end =':')
    if time < 60: # time이 60보다 작은 경우 분 단위 시간 존재하지 않으므로 "00:"출력
        print("00:", end ='')
    if sec!= 0: # sec가 0이 아니면 초 단위의 시간이 존재하므로 초 단위 시간 출력
        print(str(sec))
    if sec == 0: # sec가 0이면 초 단위 시간이 존재하지 않으므로 "00"출력
        print("00")