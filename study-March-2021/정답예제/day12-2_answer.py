## 정답 예시
movies = ["미비포유", "해리포터", "맘마미아", "어바웃타임", "라라랜드"] # 영화 목록 리스트

print("===========영화 목록===========")
for i in movies: 
	print(i)
print("==============================")
	
choice = input("예매하실 영화를 선택해주세요: ") # 영화 제목 입력

while choice not in movies: # 리스트 movies 내에 입력된 영화가 없을 경우
	print("예매할 수 없는 영화입니다")
	choice = input("예매하실 영화를 선택해주세요: ") # 영화 제목 다시 입력
	
print(f"{choice}를 선택하셨습니다") 
check = False # 인원 수가 올바른지 확인할 bool형 변수

while(not(check)):
	people = float(input("관람 인원 수를 입력해주세요: ")) # 인원을 가리키는 people변수에 실수형으로 관람 인원 입력
	if people < 0: # 입력된 인원이 음수일 경우
		print("관람 인원 수는 양수만 가능합니다")
	
	elif (people % 1) > 0: # 입력된 인원이 정수가 아닐 경우
		print("관람 인원 수는 정수만 가능합니다")
		
	else :
		people = int(people)
		check = True # 인원 수 입력이 올바르기 때문에 check는 참, 반복문 종료 

print(f"관람할 인원 수는 {people}명입니다")
	
coupon_dic = {'학생할인':3000, '지역할인':4000, '회원할인':5000} # 딕셔너리로 각 할인 쿠폰명과 가격 저장
process = True 

usage = input("할인권을 사용하시려면 y, 금액 확인으로 넘어가시려면 n을 입력해주세요: ") 

while process:
	if usage == 'y': 
		coupon = input("할인권 이름을 입력해주세요: ")
		if coupon in coupon_dic.keys(): # 입력받은 쿠폰 명이 coupon_dic의 key값에 존재하는 경우
			sale = coupon_dic[coupon] # 할인 가격 sale = coupon의 value값
			print("%d원 할인됩니다" %sale) 
			process = False # 반복문 종료
			
		else:
			print('존재하지 않는 할인권입니다')
			usage = input('할인권을 다시 입력하려면 y, 아니면 n을 입력해주세요: ')
	elif usage == 'n':
		sale = 0
		print('할인권을 사용하지 않았습니다')
		process = False # 반복문 종료
	else:
		usage = input('잘못된 입력입니다. 다시 입력해주세요: ')
		

origin_price = 12000 * people # 원래 가격 : 12000 * 관람 인원
sale_price = sale * people # 총 할인 가격 : 할인 가격 * 관람 인원
total_price = origin_price - sale_price # 총 가격 = 원래 가격 - 총 할인 가격 

print("")
print("<예매 상세 내역>")
print("==============================")
print(f'영화 제목: {choice}')
print(f'관람 인원: {people}명')
print(f'합산 금액: {origin_price}원')
print(f'할인 금액: {sale_price}원')
print("------------------------------")
print(f'실 결제액: {total_price}원')
print("==============================")