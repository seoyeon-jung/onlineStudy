## 정답 예시
def circle_a(x): # 원의 넓이를 구하는 함수 정의
    area = x * x * 3.1415
    return area

def tri_a(x, y): # 삼각형의 넓이를 구하는 함수 정의
    area = x * y / 2
    return area

def rct_a(x, y): # 직사각형의 넓이를 구하는 함수 정의
    area = x * y
    return area

def squ_a(x): # 정사각형의 넓이를 구하는 함수 정의
    area = x * x
    return area

print("==========도형 목록==========")
print("1. 원")
print("2. 삼각형")
print("3. 직사각형")
print("4. 정사각형")
print("=============================") # 메뉴 출력

menu = int(input("\n도형 목록에서 넓이를 계산할 도형의 번호를 입력해주세요: ")) # 메뉴 입력

if (menu == 1): # 조건문으로 도형 선택에 따라 함수 사용
    a = int(input("원의 반지름 길이를 입력해주세요: "))
    print("반지름 길이가 %d인 원의 넓이는 약 %.2f입니다."%(a, circle_a(a))) # 실수형 포맷코드에서 %.(숫자)f는 소수점 몇 자리까지 표기할지를 정함 
elif (menu == 2):
    a = int(input("삼각형 밑변의 길이를 입력해주세요: "))
    b = int(input("삼각형 높이의 길이를 입력해주세요: "))
    print(f"밑변이 {a}이고 높이가 {b}인 삼각형의 넓이는 {tri_a(a, b)}입니다.")
elif (menu == 3):
    a = int(input("직사각형 가로 길이를 입력해주세요: "))
    b = int(input("직사각형 세로 길이를 입력해주세요: "))
    print(f"가로가 {a}이고 세로가 {b}인 직사각형의 넓이는 {rct_a(a, b)}입니다.")
elif (menu == 4):
    a = int(input("정사각형 한 변 길이를 입력해주세요: "))
    print(f"한 변의 길이가 {a}인 정사각형의 넓이는 {rct_a(a, a)}입니다.")
else:
    print("잘못된 입력입니다.")