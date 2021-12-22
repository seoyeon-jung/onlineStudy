# chapter 04-2
# 파이썬 반복
# FOR 실습

# 코딩의 핵심
# for in <collection>
#      <Loop body>

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


for v1 in range(10):   #0부터 9까지 출력
    print('v1 is : ', v1)

for v2 in range(1, 11):  #1~10 출력
    print('v2 is : ', v2)

for v3 in range(1, 11, 2):  #1~10 중 홀수(간격 2)
    print('v3 is : ', v3)

print()


# 1~1000 합
sum1 = 0

for v in range(1, 1001):
    sum1 += v

print('1~1000 sum: ', sum1)

print('1~1000 sum: ', sum(range(1,1001)))

print('1~1000 4의 배수의 합 : ', sum(range(4,1001,4)))



# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리런 함수: range, reversed, enumerate, filter, map, zip

# 예제1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for n in names:
    print('You are: ', n)

# 예제2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for n in lotto_numbers:
    print("Current number : ", n)

# 예제3
word = "Beautiful"

for s in word:
    print("word: ", s)

# 예제4
my_info = {
    "name": "Lee",
    "Age": 33,
    "City": "Seoul"
}

for key in my_info:
    print('key: ', my_info[key])

for v in my_info.values():
    print('value: ', v)


# 예제5
name = 'FineAppLE'

for n in name:
    if n.isupper():  #isupper: 대문자 물어볼때
        print(n)
    else:
        print(n.upper())


# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 34:
        print('Found : 34!')
        break
    else:
        print('Not Found : ', num)


# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue   #boolen형 안쓸 때
    print("current type: ", v, type(v))
    print("multiply by 2: ", v*3)


# for = else
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 24:
        print("Found: 24")
        break
else:
    print("Not Found: 24")



# 구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i*j), end='')
    print()


# 변환 예제
name2 = 'Aceman'

print('Reversed', reversed(name2))
print('List', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Set', set(reversed(name2)))
