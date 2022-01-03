# 난이도 중 : **도형별 넓이 계산기**
    
# 메뉴에 있는 도형을 선택하고 길이를 입력받아 넓이를 구할 수 있는 코드를 작성해보세요.
    
# 조건 1 : 도형은 원, 삼각형, 직사각형, 정사각형이 존재합니다.
# 조건 3 : 도형 별로 필요한 길이를 입력받아야 합니다.
# 원 → 반지름
# 삼각형 → 밑변 , 높이
# 직사각형 → 가로, 세로
# 정사각형 → 한 변의 길이

import math

def circle(n):
    x = n*n*3.14
    print("반지름 길이가 %s인 원의 넓이는 약 %s입니다.\n"%(n,x))

def triangle(n,m):
    x = (n*m)/2
    print("밑변이 %s이고 높이가 %s인 삼각형의 넓이는 %s입니다.\n"%(n,m,x))

def rectangle(n,m):
    x = n*m
    print("가로가 %s이고 세로가 %s인 직사각형의 넓이는 %s입니다.\n"%(n,m,x))

def square(n):
    x = n*n
    print("한 변의 길이가 %s인 정사각형의 넓이는 %s입니다.\n"(n,x))

print("========== 도형 목록 ==========")
print("1. 원")
print("2. 삼각형")
print("3. 직사각형")
print("4. 정사각형")
print("===============================")

num = int(input("도형 목록에서 넓이를 계산할 도형의 번호를 입력해주세요: "))

if num == 1:
    n = int(input("원의 반지름 길이를 입력해주세요: "))
    circle(n)
if num == 2:
    n = int(input("삼각형의 밑변 길이를 입력해주세요: "))
    m = int(input("삼각형의 높이 길이를 입력해주세요: "))
    triangle(n,m)
if num == 3:
    n = int(input("직사각형의 가로 길이를 입력해주세요: "))
    m = int(input("직사각형의 세로 길이를 입력해주세요: "))
    rectangle(n,m)
if num == 4:
    n = int(input("정사각형 한 변의 길이를 입력해주세요: "))
    square(n)