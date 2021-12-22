# Chapter 03-3
# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형(순서 O, 중복 O, 수정 O, 삭제 O)

# 선언
a = []
b = list()
c = [70, 75, 80, 85]  #0~3까지 원소 (len사용  )
d = [1000, 10000, 'Ace', 'Base', 'Captin']
e = [1000, 10000, ['Ace', 'Base', 'Captin']]
f = [21.42, 'footbar', 3, 4, False, 3.14159]

# 인덱싱
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3])

# 리스트 연산
print('>>>>>')
print('c + d', c+d)
print('c * 3', c*3)
print("'Test' + c[0]", 'Test' + str(c[0]))

# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print()


# Identity(id)
temp = c
print(temp, c)
print(id(temp))
print(id(c))


# 리스트 수정, 삭제
print('>>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c']  #[['a', 'b', 'c']] 하나로 간주
print('c - ', c)
c[1] = ['a', 'b', 'c']  # 리스트 안에 리스트 중첩
print('c - ', c)
c[1:3] = []  # 리스트값 제거
print('c - ', c)
del c[2]  # 리스트값 제거
print('c - ', c)
print()


# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(10)  #끝부분에 데이터 삽입
print('a - ', a)
a.sort() #오름차순으로 정렬
print('a - ', a)
a.reverse()  #역순으로 출력
print('a - ', a)
print('a - ', a.index(3), a[3])
a.insert(2, 7)  #2의 자리에 7 추가 (위치, 추가할값)
print('a - ', a)
a.reverse()
print('a - ', a)
#del a[6] 비효율적
#print('a - ', a)
a.remove(10)  #지우고 싶은 데이터 선택하여 제거
print('a - ', a)
print('a - ', a.pop())  #마지막 데이터 가져오고 나머지로 다시 구성
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count("사과"))  #내가 찾는 값이 있는지 없는지
print('a - ', a.count(4))  #찾는 값이 있을 때
ex = [8, 9]
a.extend(ex)  #뒤에 ex 삽입
print('a - ', a)


# 삭제: remove, pop(끝에 있는것 제거), del(데이터 적을 때)


# 반복문 활용
while a:
    data = a.pop()
    print(data)
