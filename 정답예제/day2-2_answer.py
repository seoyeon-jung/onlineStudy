## 정답 예시

def digit_sum(x): # x의 자릿수의 합을 구하는 함수
    sum = 0 
    while x>0:
        sum += x%10 # x값을 10으로 나눈 나머지를 더함, 즉 일의 자리수를 sum에 더함
        x = x // 10 # x값을 10으로 나눈 몫을 x에 저장함. 만약 x = 1234라면 123을 x에 저장
    return sum

a = input("각 숫자를 공백으로 구분하여 입력해주세요(ex. 11 12 13): ") # 문자열 형태로 a입력
b = a.split() # 공백을 기준으로 문자열 a를 나눠 b에 리스트 형태로 저장
c = list(map(int, b)) # 리스트 b의 각 요소들을 정수형으로 변환하여 리스트 형태로 c에 저장 
#a = list(map(int, input("각 숫자를 공백으로 구분하여 입력해주세요(ex. 11 12 13): ").split()))처럼 한 줄로 사용도 가능

max = -1 # 임의로 max값을 음수로 지정
# max는 각 자릿수의 합을 비교하기 위해 사용
for x in c:
    temp = digit_sum(x) # x의 자릿수의 합을 구하는 함수 사용, temp값에 x의 자랏수의 합 저장
    if temp > max: # x의 자릿수의 합이 max보다 크다면
        max = temp # temp값을 max에 저장
        result = x # 자릿수의 합이 더 큰 수를 result에 저장

print(f'자릿수의 합이 가장 큰 수는 {result}입니다.')