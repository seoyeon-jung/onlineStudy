# 난이도 상 : **끝말잇기**
    
# 끝말잇기 게임을 할 수 있는 코드를 작성해보세요. 
    
# 조건 1 : 두 번째 단어 입력부터는 앞의 단어의 마지막 글자와 동일한 글자로 시작되어야 합니다(ex. 기차 → 차○). 만약 다른 글자로 시작하게 된다면 게임을 종료합니다.
# 조건 2 : 5의 배수 번째 단어에서는 현재까지 몇 개의 단어를 입력했는지 알려줘야 합니다.
# 조건 3 : 앞에서 입력했던 단어와 동일한 단어를 입력한다면 게임을 종료합니다.

n = input("단어를 입력하세요: ")
count = 1
n_list = [n]

while True:
    word = input("단어를 입력하세요: ")
    count += 1
    if word in n_list:
        print("앞에서 사용한 단어와 동일한 단어를 입력하셨습니다.")
        break
    elif n[-1] == word[0]:
        n_list.append(word)
        n = word
        if count % 5 == 0:
            print("(중간 점검) 현재 %d개의 단어를 입력하셨습니다"%count)
        else:
            print("틀린 단어를 입력하셨습니다. 게임을 종료합니다")
            break

## 오류나는 부분 수정 못함