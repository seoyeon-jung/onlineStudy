# Chapter 06-1
# 파이썬 클래스
# OOP(객체지향프로그래밍), self, 인스턴스 메 소드, 인스턴스 변수

# 클래스 and 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스턴스화할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재


# 예제1
class Dog :   #object 상속
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 클래스 정보
print(Dog)

# 인스턴스화
a = Dog("mikky", 2)
b = Dog("baby", 3)

# 비교
print(a == b, id(a), id(b))

# 네임스페이스
print('dog1', a.__dict__)
print('dog2', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)



# 예제2
# self의 이해
class SelfTest:
    def func1():  #클래스 매소드
        print('Func1 called')
    def func2(self):
        print('Func2 called')

f = SelfTest()

#print(dir(f)) 사용할수 있는 형식들
print(id(f))
#f.func1() : 에러발생 - 예외
f.func2()

SelfTest.func1()
#SelfTest.func2() : 에러발생
SelfTest.func2(f)  #인스턴스화된 값이 들어가야 출력가능



# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수
    stock_num = 0  # 재고

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):  #소멸할때
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before', Warehouse.__dict__)  #안에 stock_num 존재
print('>>>', user1.stock_num)

del user1
print('after', Warehouse.__dict__)  #stock_num 1 줄음




# 예제4
class Dog :   #object 상속
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self):
        return '{} says {}!'.format(self.name, sound)

# 인스턴스 생성
c = Dog('july', 4)
# 메소드 호출
print(c.info())
#메소드 호출
print(c.speak('Wal Wal'))
