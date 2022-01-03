# 난이도 중 : **OX 퀴즈 점수 계산하기**
    
# OX퀴즈의 결과가 주어졌을 때 점수를 계산하는 프로그램을 작성해보세요.
    
# 조건 1 : 'O'의 점수는 그 때까지 연속된 O의 개수를 점수로 가집니다 (ex. O → 1점, OOO → 1 + 2 + 3 = 6점)
# 조건 2 : 'X'의 점수는 0점 입니다.

n = list(input("OX 퀴즈의 결과를 입력해주세요(ex. OOXOXXO): "))

answer = 0
add = 0

for i in range(len(n)):
    if n[i] == 'O':
        if i == 0:
            add = 0
            answer += 1
        elif n[i-1] == 'O':
            add = add + 1
            answer += add + 1
        else:
            answer += 1
            add = 0

print(answer)