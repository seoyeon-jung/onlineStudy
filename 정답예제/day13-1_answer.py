## 정답 예시
num = int(input("숫자를 입력해주세요: ")) # 정수형으로 소인수분해를 진행할 숫자를 입력
d = 2 # 가장 작은 소수인 2부터 나누기

while d <= num: 
    if num % d == 0: # num이 d로 나누어떨어지면 
        print(d) # d는 num의 약수이므로 출력
        num /= d # num을 d로 나눈 값을 num에 저장
    else:
        d = d + 1 # num이 d로 나누어지지 않으면 1을 더해서 반복