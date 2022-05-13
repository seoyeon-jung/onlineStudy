# Chapter 03-2
# 파이썬 문자형
# 문자형 중요

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))


# 이스케이프 문자 사용
# I'm boy

print("I'm Boy")
print("I\'m Boy")
print('a \t b')
print('a \"\" b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)


# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()


# Raw String 출력
# 역슬래시 사용
raw_s1 = r'D:\tpython\test'

print(raw_s1)



# 멀티라인 입력
multi_str = \
'''
String
Multi line
test
'''
print(multi_str)


# 문자열 연산
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul!Daejeon!Busan!Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('z' in str_o1)
print('P' not in str_o2)


# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))


# 문자열 함수 (upper, isalnum, startswith, count, endswith, isalpha...)

print("Capitalize: ", str_o1.capitalize())  #대문자
print("endswith: ", str_o2.endswith("e"))   #마지막 문자가 무엇인지
print("replace", str_o1.replace("thon", 'Good')) # 부분 바꾸기
print("sorted: ", sorted(str_o1))  #기준에 맞게 정렬
print("split: ", str_o4.split('!'))  #!기준으로 구분


# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str))  # __iter__ : 반복가능

# 출력
for i in im_str:
    print(i)


# 슬라이싱
str_s1 = "Nice Python"

# 슬라이싱 연습
print(str_s1[0:3])  # 3-1까지 나옴(0,1,2번)
print(str_s1[5:])  # 5부터 맨끝까지 나옴
print(str_s1[:len(str_s1)])  # str_s1[:11]과 동일
print(str_s1[:len(str_s1)-1])  # str_s1[:10]과 동일
print(str_s1[1:4:2])  #마지막 숫자:단위
print(str_s1[-5:])  #뒤부터 센 것
print(str_s1[1:-2])  #1부터 뒤에서 3번째까지
print(str_s1[::2])  #처움부터 끝가지 2칸 간격으로
print(str_s1[::-1])  #거꾸로 표현


# 아스키 코드(또는 유니코드)
a = 'z'

print(ord(a))  #아스키코드로
print(chr(122))  #숫자로
