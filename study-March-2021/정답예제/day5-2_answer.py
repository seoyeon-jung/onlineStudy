## 정답 예시

w_lst = [] # 입력받은 단어를 저장할 리스트
count = 0 # 단어 개수

word = input() # 첫 번째 단어 입력
w_lst.append(word) # w_lst에 첫 번째 단어 저장

while True:
    word = input() # 단어 입력
    if word[0] != w_lst[count][-1]: # 앞의 단어 마지막 글자와 현재 단어의 첫 번째 글자 비교
        print("틀린 단어를 입력하셨습니다. 게임을 종료합니다.")
        break
    if word in w_lst: # 동일한 단어가 이미 입력되었는지 확인 
        print("앞에서 사용한 단어와 동일한 단어를 입력하셨습니다. 게임을 종료합니다.")
        break
    if (count+1) % 5 == 4: # 현재 단어가 5의 배수만큼 입력되었다면 중간 점검
        print("(중간 점검) 현재 %d개의 단어를 입력하셨습니다." %(count+2))
    w_lst.append(word) # 앞에서 프로그램이 종료되지 않았다면 올바른 단어를 입력한 것이므로 w_lst에 단어 추가 
    count += 1 # 입력한 단어 개수## 정답 예시
w_lst = [] # 입력받은 단어를 저장할 리스트
count = 0 # 단어 개수

word = input() # 첫 번째 단어 입력
w_lst.append(word) # w_lst에 첫 번째 단어 저장

while True:
    word = input() # 단어 입력
    if word[0] != w_lst[count][-1]: # 앞의 단어 마지막 글자와 현재 단어의 첫 번째 글자 비교
        print("틀린 단어를 입력하셨습니다. 게임을 종료합니다.")
        break
    if word in w_lst: # 동일한 단어가 이미 입력되었는지 확인 
        print("앞에서 사용한 단어와 동일한 단어를 입력하셨습니다. 게임을 종료합니다.")
        break
    if (count+1) % 5 == 4: # 현재 단어가 5의 배수만큼 입력되었다면 중간 점검
        print("(중간 점검) 현재 %d개의 단어를 입력하셨습니다." %(count+2))
    w_lst.append(word) # 앞에서 프로그램이 종료되지 않았다면 올바른 단어를 입력한 것이므로 w_lst에 단어 추가 
    count += 1 # 입력한 단어 개수