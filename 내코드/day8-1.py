# 난이도 중 : **직사각형 넓이와 둘레**
    
# 직사각형에 대한 클래스를 만들고, 가로와 세로 길이를 입력받아 그에 대한 넓이와 둘레를 출력해보세요.
    
# 조건 1 : 클래스에서 생성자를 통해 가로, 세로 길이를 초기화
# 조건 2 : 클래스 내에 둘레와 넓이를 구하는 기능은 메소드를 포함

class rect:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def round(self):
        answer = self.w * 2 + self.h * 2
        return answer
    def area(self):
        answer = self.w * self.h
        return answer

w = int(input("가로: "))
h = int(input("세로: "))

n = rect(w, h)

print("직사각형의 둘레는 %d이고, 넓이는 %d입니다."%(n.round(), n.area()))