'''
- 난이도 중 : **2021년 a월 b일은 무슨 요일**
    
    날짜를 입력받고, 2021년을 기준으로 입력받은 날짜가 무슨 요일인지 구하는 프로그램을 작성해봅시다.
    
    - 조건 1 : 2021년 1월 1일은 금요일입니다
    - 조건 2 : 2021년은 윤년이 아닙니다.
'''

month_list = {'1':31, '2':28, '3':31, '4':30, '5':31, '6':30,
              '7':31, '8':31, '9':30, '10':31, '11':30, '12':31}
month = input("월: ")
day = input("일: ")

answer_month = 0

if int(month) == 1:
    answer_month = 0
else:
    for i in range(1, int(month)):
        answer_month = answer_month + month_list['{}'.format(i)]

answer_day = answer_month+int(day)

if answer_day % 7 == 0:
    print("{}월 {}일은 목요일입니다.".format(month, day))
elif answer_day % 7 == 1:
    print("{}월 {}일은 금요일입니다.".format(month, day))
elif answer_day % 7 == 2:
    print("{}월 {}일은 토요일입니다.".format(month, day))
elif answer_day % 7 == 3:
    print("{}월 {}일은 일요일입니다.".format(month, day))
elif answer_day % 7 == 4:
    print("{}월 {}일은 월요일입니다.".format(month, day))
elif answer_day % 7 == 5:
    print("{}월 {}일은 화요일입니다.".format(month, day))
else:
    print("{}월 {}일은 수요일입니다.".format(month, day))