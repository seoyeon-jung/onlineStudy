# 난이도 중
# 문장 내 단어 오름차순으로 출력하기
# 공백을 기준으로 단어를 구분한 후 중복 단어를 삭제하여 오름차순으로 출력해보세요

answer = set(input("문장을 입력하세요: ").split())
answer = list(answer)
answer.sort()
print(answer)