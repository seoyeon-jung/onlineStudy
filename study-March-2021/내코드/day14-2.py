"""
- 난이도 상 : **오름차순 정렬하기**
    
    sort 키워드를 사용하지 않고, 입력받은 숫자를 오름차순으로 정렬하는 프로그램을 작성해주세요.
    
    - 오름차순 : 작은 것 → 큰 것 순서대로 정렬하는 것
    - 조건 1 : 출력값은 리스트 자료형으로 출력합니다.
    - 조건 2 : 숫자는 5개의 숫자를 입력받습니다.
"""

number = []

for i in range(5):
    num = int(input("숫자를 입력하세요: "))
    number.append(num)

for i in range(len(number)):
    for j in range(i+1, len(number)):
        if number[i] > number[j]:
            number[i], number[j] = number[j], number[i]

print(number)