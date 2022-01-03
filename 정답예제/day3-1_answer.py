## 정답 예시
num = int(input("삼각형의 높이를 입력해주세요: ")) # 정수형으로 삼각형 길이 입력받기

for i in range(0, num): # 입력받은 길이 만큼 반복
	# 삼각형 모양을 위해 반복문이 실행될 때마다 별의 개수가 늘어야 함 
	for j in range(0, num-1-i): #오른쪽부터 별이 찍혀야 하므로, 그만큼의 공백을 출력
		print(' ',end='') 
	
	for k in range(0, i+1):
		print('*',end='') 
	print("")