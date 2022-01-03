## 정답 예시
a = input("숫자 두 개를 입력해주세요(ex. '3 5'): ")
b= int(input("배수를 알고 싶은 숫자를 입력해주세요: ")) 

num1 = int(a.split(' ')[0]) # 두 숫자를 리스트 형태로 변환, 첫 번째 숫자를 정수형으로 num1에 저장 
num2 = int(a.split(' ')[1]) # 두 숫자를 리스트 형태로 변환, 두 번째 숫자를 정수형으로 num2에 저장 

for i in range(num1, num2+1): # num1부터 num2까지 반복
    if i % b == 0: 
        print(i, end = ' ') # i가 b의 배수이면 출력