# 난이도 중 : **숫자 n의 k번째 약수**
    
# 숫자 n과 k를 입력받아, n의 k번째 약수를 구해보세요.
    
# 조건 1 : 숫자 k는 n의 약수의 개수보다 작아야합니다. 만일 k가 n의 약수의 개수보다 크다면 오류 메시지를 출력해주세요

n = int(input("숫자를 입력해주세요: "))
k = int(input("몇 번째 약수를 알고 싶은지 입력하세요: "))

num = []

for i in range(1, n+1):
    if n % i == 0:
        num.append(i)

if len(num) < k:
    print("입력하신 숫자만큼의 약수가 존재하지 않습니다.")
else:
    print("{}의 {}번째 약수는 {}입니다.".format(n, k, num[k-1]))