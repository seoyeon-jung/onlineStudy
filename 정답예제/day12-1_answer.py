## 정답 예시
def mul_table(x): # 함수를 출력하는 함수
    for i in range(1, 10): # 1이상 10미만의 정수
        print("%d × %d = %d"%(x, i, i*x)) 

while True :
    num = int(input("\n2부터 9사이 숫자를 입력해주세요. (1을 누르면 프로그램이 종료됩니다) "))
    if num == 1: 
        print("프로그램을 종료합니다.")
        break
    elif num > 9 or num < 1: 
        print("범위 외의 숫자입니다.")
    else: 
        mul_table(num)