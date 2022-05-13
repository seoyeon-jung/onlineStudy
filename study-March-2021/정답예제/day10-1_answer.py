## 정답 예시
sec = int(input("초 단위의 시간을 입력해주세요: ")) # 초 단위 시간 입력
print(str(sec) + "초 ", end ='= ')

if sec>=86400:
    temp = sec // 86400 # temp에 sec(초)를 86400으로 나눠서 구한 일수를 저장
    sec -= temp*86400 # sec(초)에서 일수(temp) * 86400만큼 뺄셈
    print(str(temp) + '일', end =' ') 

if sec>=3600:
    temp = sec // 3600 # temp에 sec(초)를 3600으로 나눠서 구한 시간을 저장
    sec -= temp*3600 # sec(초)에서 시간(temp) * 3600만큼 뺄셈
    print(str(temp) + '시간', end =' ')

if sec>=60:
    temp = sec // 60 # temp에 sec(초)를 60으로 나눠서 구한 분을 저장
    sec -= temp*60 # sec(초)에서 분(temp) * 60만큼 뺄셈
    print(str(temp) + '분', end =' ')

if sec!=0:
    print(str(sec) + '초') # 앞의 시간들을 제외하고 남은 sec(초) 출력