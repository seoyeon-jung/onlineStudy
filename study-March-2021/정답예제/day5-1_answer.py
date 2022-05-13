## 정답 예시

answer = list(input("OX퀴즈의 결과를 입력해주세요(ex.OOXOXXO): "))
# 문자열로 OX게임의 결과를 입력받고, list형태로 저장

total = 0 # 총 점수
current = 1 # 현재 O의 점수

for i in answer:
	if i == 'O':
		total += current 
		current += 1 # O의 현재 점수 1점 추가 
	elif i == 'X':
		if current>1:
			current = 1 # O의 현재 점수 초기화
	
print(total)