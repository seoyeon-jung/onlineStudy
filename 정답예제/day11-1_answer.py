## 정답 예시
word = input()
mid_word = '' # 가운데 글자를 저장할 문자열

if len(word)%2 == 0: # 입력받은 단어의 길이가 짝수일 경우
    num = len(word)//2 # 단어 길이를 2로 나눈 몫을 num에 저장
    mid_word += word[num - 1] + word[num] # num-1번째, num번째 단어를 mid_word에 추가
else: # 입력받은 단어의 길이가 홀수일 경우
    num = len(word) // 2 # 단어 길이를 2로 나눈 몫을 num에 저장
    mid_word += word[num] # num번째 단어를 mid_word에 추가

print(mid_word)