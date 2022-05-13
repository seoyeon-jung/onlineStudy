# 난이도 중 : **시간 변환 계산기**
    
# 초 단위의 시간을 입력 받고, 일, 시, 분, 초로 시간을 계산하여 출력하는 코드를 작성해보세요.
# 사용하지 않는 단위는 출력하지 않습니다 (ex. '3601'초를 입력하면 '1시간 0분 1초'가 아닌 '1시간 1초'로 출력)
# 1일 = 86400초
# 1시간 = 3600초
# 1분 = 60초

day = int(input("초 단위의 시간을 입력해주세요: "))

hour = day  //3600

if hour > 0:
    minute = (day - (hour*3600))  // 60
    if minute > 0:
        second = day - (hour*3600) - (minute*60)
        print("{}초 = {}시간 {}분 {}초".format(day,hour,minute,second))
    else:
        second = day - (hour*3600)
        print("{}초 = {}시간 {}초".format(day,hour,second))
else:
    minute = day  //60
    if minute > 0:
        second = day - (minute*60)
        print("{}초 = {}분 {}초".format(day,minute,second))
    else:
        second = day - (minute*60)
        print("{}초 = {}초".format(day,second))