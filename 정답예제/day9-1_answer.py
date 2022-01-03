## 정답 예시
n = int(input("숫자를 입력해주세요: "))
k = int(input("몇 번째 약수를 알고 싶은지를 입력해주세요: "))

lst = [] # n의 약수를 저장할 리스트

for i in range(1, n+1): # 1에서 n까지
    if(n%i==0): # n에서 i를 나눴을 때 나머지가 0이면 i는 n의 약수임
        lst.append(i)
if(len(lst) < k): # k가 약수의 개수보다 클 경우를 확인
    print("입력하신 숫자 만큼의 약수가 존재하지 않습니다.")
else: 
    print(f"{n}의 {k}번째 약수는 {lst[k-1]}입니다.") 
    # 파이썬은 순서를 0부터 세기 때문에 lst[k-1]