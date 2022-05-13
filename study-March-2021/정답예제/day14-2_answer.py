## 정답 예시
lst = [] # 각 숫자를 저장할 리스트

for i in range(5):
    a = int(input("숫자를 입력하세요: "))
    lst.append(a) # 리스트에 숫자 추가

for i in range(0, len(lst)-1): # 0부터 리스트 길이-2, 즉 4번 반복
    min_i = i # 최소 숫자의 인덱스 값을 저장할 min_i
    for j in range(i+1, len(lst)): 
        if lst[j] < lst[min_i]: # j번째 숫자가 min_i번째 숫자보다 작을 경우
            min_i = j # 최소 숫자의 인덱스인 min_i에 j값 저장
    lst[i], lst[min_i] = lst[min_i], lst[i] # min_i값을 i번째에 저장함

# 파이썬에서 a, b = b, a를 사용하면 a와 b의 값을 서로 바꿀 수 있음

print(lst)