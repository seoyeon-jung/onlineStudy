## 정답 예시

a = input("문장을 입력해주세요: ")   # 문장 입력
b = a.split('.')              # 마침표를 기준으로 문장 나누기

for i in range(len(b)-1):     # for문을 통해 각 문장 별로 살펴보기
    c = b[i].strip()          # 각 문장의 좌우 끝 공백 제거하기
    d = c.split(' ')          # 공백을 기준으로 단어 나누기
    for j in range(len(d)):   # for문을 통해 각 단어 살펴보기
        d[j] = d[j].lower()   # 모든 단어의 알파벳 소문자로 변환
        if d[j] == 'i': 
            d[j] = 'I'        # 'i'만 존재하는 경우 대문자 'I'로 변환
        elif d[j][0:2] == "i'":
            d[j]= d[j].replace('i','I') # "i'"로 존재하는 경우 대문자 'i'를 'I'로 변환
    d[0] = d[0].capitalize()  # 문장 첫 번째 단어의 첫 번째 문자를 대문자료 변환
    d= ' '.join(d)            # 리스트 형태의 단어들을 문자열로 변환
    print(d, end = '. ')      # 문장 출력하고 끝에 end 키워드를 통해 마침표 찍어주기