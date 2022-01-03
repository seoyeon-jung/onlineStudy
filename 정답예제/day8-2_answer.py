## 정답 예시 (그 날 안풀었음)
class Point:
    def __init__(self, x, y): # 객체에서 사용할 초깃값 설정 
        self.x = x
        self.y = y
    def set_x(self, x): # x좌표 설정
        self.x = x
    def set_y(self, y): # y좌표 설정
        self.y = y
    def get(self): # x, y좌표 반환
        return self.x, self.y
    def move(self, dx, dy):
        self.x += dx # x좌표 dx만큼 이동
        self.y += dy # y좌표 dy만큼 이동

x = int(input("x좌표를 입력해주세요: "))
y = int(input("y좌표를 입력해주세요: "))
a = Point(x, y) # 초깃값 설정
print("현재 좌표 :", a.get())

print("\nx좌표 설정을 원한다면 x, y좌표 설정을 원한다면 y, 좌표 이동을 원한다면 m, 좌표 설정을 종료하려면 0을 입력해주세요.")
while True:
    u = input("\n입력: ")
    if u == 'm':
        dx = int(input("x좌표를 얼마만큼 이동할지 입력해주세요: "))
        dy = int(input("y좌표를 얼마만큼 이동할지 입력해주세요: "))
        a.move(dx, dy)
    elif u == 'x':
        x = int(input("x좌표를 입력해주세요: "))
        a.set_x(x)
    elif u == 'y':
        y = int(input("y좌표를 입력해주세요: "))
        a.set_y(y)
    elif u == '0':
        break
    else: 
        print("잘못된 입력입니다.")

print("현재 좌표 :", a.get())