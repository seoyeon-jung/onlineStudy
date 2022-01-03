# 난이도 상 : **뒤집은 소수**
    
# 여러 숫자를 입력받고, 각 숫자가 뒤집었을 때 소수이면 출력을 하는 프로그램을 만들어보세요. 
    
# 조건 1 : 숫자를 뒤집었을 때 소수이면 출력을 합니다 (ex. 32를 뒤집었을 때 23이고, 23은 소수이므로 출력)
# 조건 2 : 최소 두 개 이상의 함수를 사용해주세요.

n_list = []
n = [2, 3, 5, 7, 9]

def n_change(n_list):
    for i in n_list:
        s = int(i[::-1])
        prime(i, s)

def prime(x, y):
    m = []
    for j in n:
        if y % j == 0:
            break
        else:
            if x not in m:
                m.append(x)
                print(x, end=" ")

count = int(input("입력받을 숫자의 개수를 입력해주세요: "))

i = 1

while i < count + 1:
    num = input("각 %d번째 숫자를 입력해주세요: "%(i))
    n_list.append(num)
    i += 1

n_change(n_list)