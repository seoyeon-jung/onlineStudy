## 정답 예시
def reverse(x): 
    x = list(str(x)) # 숫자 x를 문자열로 변환하고 리스트 형태로 저장
    x.reverse() # reverse 함수를 통해 각 자리의 순서를 바꿈
    rx = ''.join(x) # rx에 x를 합쳐 문자열의 형태로 저장 
    return int(rx) # rx를 정수형으로 반환

def is_prime(x):
    for i in range(2, x+1): # 2부터 x까지 반복
        prime = True # 소수를 True로 저장
        for j in range(2, i): # 2부터 i-1까지 반복
            if i % j == 0: # i가 j로 나누어지면 x는 i외의 약수를 가지게 되므로 소수가 아니게 됨
                prime = False
                break
    return prime 
    
num = int(input("입력받을 숫자의 개수를 입력해주세요: ")) 
lst = []

for i in range(num): # num개 만큼의 숫자를 lst에 저장
    temp = int(input("각 %d번째 숫자를 입력해주세요: " %(i+1))) 
    lst.append(temp)

for i in lst: # lst에 저장된 각 요소를 함수에 입력
    if is_prime(reverse(i)): # 뒤집은 수가 소수인지 확인
        print(i, end = " ")

# 정답 예제가 올바르게 출력되지 않는다 (해결해야함)