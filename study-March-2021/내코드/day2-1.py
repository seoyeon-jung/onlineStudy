# 난이도 중 : **반올림 계산기 만들기**
    
# 파이썬에 내장된 round() 함수를 이용하지 않고, 반올림 계산을 실행할 수 있는 코드를 작성해보세요.
    
# 조건 1 : 소수 첫째 자리에서 반올림이 이루어집니다. (ex. 3.14 → 3, 1.5 → 1)
# 조건 2 : 소수 첫째 자리가 0~4이면 버림, 5~9이면 올림을 합니다.

number = input("숫자를 입력해주세요: ").split(".")

if int(number[1][0]) >= 5:
    print(int(number[0])+1)
else:
    print(number[0])