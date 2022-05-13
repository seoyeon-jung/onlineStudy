# Chapter 07-1
# 파이썬 예외처리의 이해
# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError...
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계) 발생하는 예외도 중요
# 1) 예외는 반드시 처리
# 2) 로그는 반드시 남긴다 (로그-에러가 발생했다는 증거)
# 3) 예외는 던져진다 (다른곳으로 위임가능)
# 4) 예외 무시 가능 (좋지 않은 습관)



# SyntaxError : 문법 오류
# print('erro)
# print('error'))
# if True
#        pass


# NameError : 참조 없음
#a = 10
#b = 15
#print(c)


# ZeroDivisionError : 0으로 나눌수 없음
# print(100/0)



# IndexError
# x = [50, 60, 70]
# print(x[1])
# print(x[4])
# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop())


# KeyError (주로 딕셔너리에서 발생)
# dic = {'name' : 'Lee', 'Age' : 41, 'City' : 'Busan'}
#  print(dic['hobby'])  _불가능함
# print(dic.get('hobby'))  #존재하지 않으면 None이라고 출력



# 예외 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생 시 예외 처리 권장(EAFP)


# AttratibuteError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
# import time
#print(time.time2())  #존재하지 않는 걸 나타내려고 할 때


# ValueError
# x = [10, 50, 90]
# x.remove(50)
# print(x)
# x.remove(200)  _데이터가 존재하지 않을 때


# FileNotFoundError
# f = open('test.txt')   _파일이 존재하지 않을 때


# TypeError : 자료형에 맞지 않는 연산을 수행할 경우
# x = [1, 2]
# y = (1, 2)
# z = 'test'

# print(x+y)  _데이터 하나로 합치기 _불가능함
# print(x+z)  _리스트와 문자형 합치기 불가능
# print(y+z)

# print(x + list(y))
# print(x + list(z))



# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except 에러명1: 여러개 가능
# except 예외명2
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 마지막에 실행


name = ['Kim', 'Lee', 'Park']

# 예제1
# try:
#    z = 'Kim'
#    x = name.index(z)
#    print('{} Found it! {} in name'.format(z, x + 1))
# except ValueError:
#    print('Not Fount it! - Occurred ValueError!')
# else:
#    print('OK! else.')

print()


# 예제2
#try:
#    z = 'Cho'
#    x = name.index(z)
#    print('{} Found it! {} in name'.format(z, x + 1))
#except:
#    print('Not Fount it! - Occurred ValueError!')
#else:
#    print('OK! else.')

print()


# 예제3
#try:
#    z = 'Cho'
#    x = name.index(z)
#    print('{} Found it! {} in name'.format(z, x + 1))
#except Exception as e:
#    print(e)
#    print('Not Fount it! - Occurred ValueError!')
#else:
#    print('OK! else.')
#finally:
#    print('OK! finally!')  #에러 발생해도 출력

print()



# 예제4
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Park'
    if a == 'Kim':
        print('OK! Pass!')
    else:
        raise ValueError
except ValueError:
    print('Occured Exception!')
else:
    print('Ok! else!')
