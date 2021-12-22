# Chapter02-1
# 파이썬 완전 기초
# Print 사용
# 참조: https://www.python-course.eu/python3_formatted_output.python3_formatted_output

# 기본 출력
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

print()


# separator 옵션
print('P','Y', 'T', 'H', 'O', 'N', sep='')
print('010', '7777', '1234', sep='-')
print('python', 'google.com', sep='@')

print()


# end 옵션 : 줄바꿈 안하고 라인을 길게 하려 사용
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site', end=' ')

print()


# file 옵션
import sys

print('Learn Python', file=sys.stdout)
print()


# format 사용(d(정수), s(문자열), f(실수))
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 2))
print('{1} {0}'.format('one', 'two'))

print()



# %s이용
print('%10s' % ('nice'))  #10자리 띄고 채우기
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))  #왼쪽부터 채우기
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))  #원하는 기호로 앞 채움
print('{:^10}'.format('nice'))   #중앙정렬

print('%.5s' % ('pythonstudy'))  #5글자만
print('%5s' % ('pythonstudy'))
print('{:10.5}'.format('pythonstudy'))  #5글자

print()


# %d이용
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))

print()


# %f이용
print('%f' %(3.14343434343434))
print('{:f}'.format(3.14343434343434))

print('%06.2f' % (3.141592653589793))  #총자리6소수2
print('{:06.2f}'.format(3.141592653589793))

print()
