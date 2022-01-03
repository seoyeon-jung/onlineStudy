## 정답 예시
class Rectangle:
    def __init__(self, width, height): # 직사각형의 가로, 세로 길이 초깃값 설정
        self.width = width
        self.height = height
    def area(self): # 직사각형의 넓이를 구하는 메소드
        return self.width * self.height
    def round(self):# 직사각형의 길이를 구하는 메소드
        return (self.width + self.height)*2

w = int(input("가로: "))
h = int(input("세로: "))
a = Rectangle(w, h) # 클래스의 객체 a 생성

print("직사각형의 둘레는 %d이고, 넓이는 %d입니다." %(a.round(), a.area()))