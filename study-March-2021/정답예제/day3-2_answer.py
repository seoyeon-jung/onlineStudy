## 정답 예시

print("\t\t\t   <3월 달력>")
start_day = 1  # 월요일부터 시작이므로 1 
# 일요일일 경우 start_day = 0, 화요일일 경우 2... , 토요일일 경우 6
last_date = 31 # 31일까지 존재하므로 last_date = 31

print('\t일\t월\t화\t수\t목\t금\t토')
for i in range(start_day): # 월요일이 시작하는 날짜이므로 하루 만큼의 공백 출력
	print('\t', end='')
for i in range (1, last_date+1): # 1부터 31까지 반복해야하므로 range는 (1, 32)가 되어야 함
	if (i % 7 != 6):
		print('\t%d' %i, end='')
	elif (i % 7 == 6): # i를 7로 나눈 나머지가 6일때는날짜는 토요일이므로 개행을 해줘야 함
		print('\t%d\n' %i)