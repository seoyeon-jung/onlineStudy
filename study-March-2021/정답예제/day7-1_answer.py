## 정답 예시
word = input()

word = list(set(word)) # 집합 자료형을 통해 중복된 알파벳 삭제
word.sort() # 오름차순 정렬
print(word)