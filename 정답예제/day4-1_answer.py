## 정답 예시
num = int(input("숫자를 입력해주세요: "))

fac = 1 
for i in range(1, num+1): 
    fac *= i # 1부터 num까지의 숫자를 차례대로 곱함

print("%d!은 %d입니다." %(num, fac))