# 난이도 중 : **가운데 글자 찾기**
    
# 단어를 입력받고, 입력받은 단어의 가운데 글자를 찾는 코드를 작성해보세요.
    
# 조건 1 : 단어의 길이가 홀수이면 가운데 글자 하나를 출력합니다.
# 조건 2 : 단어의 길이가 짝수이면 가운데 글자 두 개를 출력합니다.

word = input()
n = len(word)

if n % 2 == 0:
    print(word[int(n/2 - 1)], word[int(n/2)])
else:
    print(word[int(n/2)])