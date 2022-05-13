"""
- 난이도 중 : **소인수분해**
    
    정수를 소수의 곱만으로 표현하는 것을 소인수분해라고 합니다. 
    
    소인수분해 프로그램을 작성해보세요.
"""

num = int(input("숫자를 입력해주세요: "))

for i in range(2, num):
    while num % i == 0:
        num /= i
        print(i)