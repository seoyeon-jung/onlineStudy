# 난이도 중 : **함수를 활용한 구구단**
    
# 함수를 활용하여 구구단 프로그램을 만들어보세요.
    
# 조건 1 : 프로그램을 종료하기 전까지 계속 반복되어야 합니다.
# 조건 2 : 숫자를 입력받아 해당 숫자의 구구단을 출력해야 합니다.
# 조건 3 : 입력받는 숫자의 범위는 2에서 9까지입니다.  범위 이외의 숫자를 입력하면 오류 표시를 해야합니다.
# 조건 4 : 함수를 하나 이상 만들어서 사용해야합니다.

def answer(num):
    for i in range(1,10):
        print("{} X {} = {}".format(num,i,num*i))

while True:
    num = int(input("2부터 9사이 숫자를 입력해주세요(1을 누르면 프로그램이 종료됩니다.): "))
    if num == 1:
        print("프로그램을 종료합니다.")
        break
    elif num == 0:
        print("범위 외의 숫자입니다.")
        print()
    elif num > 9:
        print("잘못된 입력입니다.")
        print()
    else:
        answer(num)
        print()