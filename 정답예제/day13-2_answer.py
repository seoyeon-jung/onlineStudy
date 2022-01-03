## 정답 예시 (그 때 안풀었음)

s = input("단어를 입력해주세요: ")

front = [] # 앞의 글자를 비교하기 위한 리스트
behind = [] # 뒤의 글자를 비교하기 위한 리스트

result = True # 회문이 맞는지 아닌지 

for i in s: # 각 리스트에 문자열의 각 문자 추가
    front.append(i)
    behind.append(i)

while front: # front 리스트에 요소가 남아있는 동안
    if front.pop(0) != behind.pop(): # front 리스트의 첫 문자와 behind 리스트의 마지막 문자 비교 
        result = False # 만약 두 문자가 다르면 회문이 아니므로 result = False

if result:
    print("%s는 회문입니다." %(s))
else:
    print("%s는 회문이 아닙니다." %(s))