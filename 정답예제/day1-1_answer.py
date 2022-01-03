## day 1-1 정답 예시

a = input("문장을 입력해주세요: ")  # 문장 입력
b = a.split(' ')  # 공백을 기준으로 문장 속 단어 나누기
b = set(b)  # b의 자료형 집합 자료형으로 바꾸어 중복 제거
b = list(b)  # list형으로 자료 다시 반환
b.sort()  # sort 함수를 통해 단어 오름차순 정렬

for i in b:
    print(i, end = ' ')  # 각 단어 출력