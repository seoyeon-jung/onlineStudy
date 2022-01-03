# 난이도 상 : **3월 달력 출력하기**
    
# 반복문과 조건문을 활용하여 2021년 3월의 달력을 출력해보세요.
    
# 조건 1 : 3월의 마지막 날은 31일이며, 3월 1일은 월요일입니다.
# 조건 2 : 달력은 일요일부터 시작되며, 날짜 위에 요일 표시를 출력해야 합니다.

print("<3월 달력>\n")
print("일  월  화  수  목  금  토")

for i in range(0, 32, 7):
    for j in range(i, i+7):
        if j == 0:
            print("  ", end="  ")
        elif j > 31:
            break
        elif j < 10:
            print(j, end = "   ")
        else:
            print(j, end="  ")
    print()