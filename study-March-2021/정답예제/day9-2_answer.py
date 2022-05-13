## 정답 예시
n = int(input("총 과목의 수를 입력해주세요: ")) # 과목의 개수 입력
sum = 0 # 과목 총점

for i in range(n):
    score = int(input("점수를 입력해주세요: ")) # 각 과목의 점수 입력
    
    if score > 100 or score < 0: # 점수별 등급
        print("잘못된 점수 입력입니다.")
    elif score < 60:
        print("해당 과목 등급: F")
    elif score < 70:
        print("해당 과목 등급: D")
    elif score < 80:
        print("해당 과목 등급: C")
    elif score < 90:
        print("해당 과목 등급: B")
    else:
        print("해당 과목 등급: A")

    sum += score

print("총 과목의 평균은 %d점 입니다." %(sum / n))