# 난이도 상 : **전자레인시 시간 설정하기**
    
# 전자레인지의 시간을 입력하여 설정하는 코드를 작성해보세요.
    
# 조건 1 : 시간 버튼은 각 10초, 30초, 1분, 10분이 존재합니다.
# 조건 2 : 이 외의 숫자를 입력하면 오류 메시지를 출력합니다.
# 조건 3 : 버튼을 누르면 본래 시간에서 누르는 버튼만큼의 시간을 추가합니다.
# 조건 4 : 시간이 추가될 때마다 현재 입력된 총 시간을 출력합니다.

print("1. 10초    2. 30초    3. 1분    4. 10분    5. 시작")

minute = 0
second = 0

while True:
    time = int(input("원하는 시간의 숫자 버튼을 입력해주세요: "))

    if time == 1:
        second = second+10
        if second > 60:
            minute = minute+1
            second = second-60
        print(str(minute)+":"+str(second))
    elif time == 2:
        second = second+30
        if second > 60:
            minute = minute+1
            second = second-60
        print(str(minute)+":"+str(second))
    elif time == 3:
        minute = minute+1
        print(str(minute)+":"+str(second))
    elif time == 4:
        minute = minute+10
        print(str(minute)+":"+str(second))
    elif time == 5:
        print()
        print("전자레인지를 작동합니다.")
        break
    else:
        print("잘못된 입력입니다.")