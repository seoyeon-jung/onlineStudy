# 난이도 중 : **영어 단어에 사용된 알파벳 오름차순으로 정리하기**
    
# 영어 단어를 입력받고, 단어에 사용된 알파벳을 중복없이 오름차순으로 정렬하여 출력해보세요.
    
# 조건 1 : 리스트가 아닌 묶음 자료형을 활용해보세요.
# 조건 2 : 출력은 리스트 형태로 출력합니다.

word = input()
n = {}
m = []

for i in range(len(word)):
    n[word[i]] = i

n_list = dict(sorted(n.items(), key = lambda x: x[0]))

for i in n_list.keys():
    m.append(i)

print(m)