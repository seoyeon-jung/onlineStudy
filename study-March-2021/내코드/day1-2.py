# 난이도 상
# 영어 대소문자 올바르게 사용하기

#여러 영어 문장을 입력받았을 때, 문장의 대소문자 사용을 올바르게 고치는 프로그램을 만들어보세요.

# 조건 1 : 문장은 마침표(.)를 기준으로 구분됩니다.
# 조건 2 : 각 문장의 첫 번째 글자와, '나'를 뜻하는 단어 'I'는 무조건 대문자여야 합니다.
# 조건 3 : 이외의 글자는 소문자여야 합니다.


text = input("문장을 입력해주세요: ")
text = text.lower()
text = text.split('. ')

result = ""

for i in text:
    i = i.capitalize()
    if result == "":
        result = i
    else:
        result = result+" "+i

print("corrected sentece: " + result)