# 난이도 상 : **두 숫자 사이 n의 배수 찾기**
    
# 공백으로 구분된 문자열 형태의 두 숫자를 입력받고, n을 입력받아 두 숫자 사이에 존재하는 n의 배수를 구해보세요.
    
# 조건 1 : 숫자 두 개는 공백(스페이스 바)로 구분되어 입력됩니다.
# 조건 2 : 숫자 두 개는 문자열 형태로 입력됩니다.
# 조건 3 : 입력된 숫자를 포함하여 배수를 출력해보세요.

num = input("숫자 두 개를 입력해주세요. (ex. '3 5): ").split( )
multiple = int(input("배수를 알고 싶은 숫자를 입력해주세요: "))

result = []
i = 1

while True:
    if multiple * i < int(num[0]):  # 배수를 알고 싶은 숫자가 범위 내 숫자보다 작을 경우
        i += 1
    elif multiple * i >= int(num[0]):  # 배수를 알고 싶은 숫자가 범위 내 숫자일 경우
        if multiple * i <= int(num[1]) + 1:
            result.append(multiple * i)
            i += 1
        elif multiple * i > int(num[1]) + 1:  #배수를 알고 싶은 숫자가 범위보다 클 경우
            break

print(*result, sep=", ")