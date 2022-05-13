## 정답 예시 (그 날 안풀었음)
menu = {'물' : [700, 5], '콜라' : [1000, 0], '사이다' : [1000, 3], '과일 주스':[800, 2]}
# key 값에 음료 이름, value 값에 리스트형으로 [음료 가격, 음료 개수] 지정

print("======음료수 목록======")
print("물\t\t 700원")
print("콜라\t\t1000원")
print("사이다\t\t1000원")
print("과일 주스\t 800원")
print("======================")

money = int(input("소지하고 계신 돈의 액수를 입력해주세요: "))
choice = input("마시고 싶은 음료를 입력해주세요: ")
if choice in menu: # 음료가 메뉴 안에 존재하는지 확인
    print("%s의 가격은 %d원입니다."%(choice, menu[choice][0])) 
# menu[choice][0]에서 choice가 menu의 key값이므로 value를 불러냄. 
# 각 value의 첫 번째 요소인 가격 호출.
    if menu[choice][1] == 0: # value의 두 번째 요소인 개수가 0일 경우 품절
        print("현재 해당 음료는 품절 상태입니다.")
    else: 
        if money < menu[choice][0]: # 소지금이 음료 가격보다 적을 경우
            print("돈이 부족합니다.")
        else:
            print("주문이 완료되었습니다.") 
            print("잔액은 %d입니다." %(money - menu[choice][0])) # 소지금 - 가격
else:
    print("해당 음료가 존재하지 않습니다.")