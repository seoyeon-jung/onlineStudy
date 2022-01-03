# 난이도 상 : **과목 점수에 따른 등급과 평균**
    
# 시험 점수를 입력받고, 그에 따른 등급과 총 평균을 계산하는 프로그램을 작성해주세요.
    
# 조건 1 : 시험 점수는 0에서 100점 사이입니다.
# 조건 2 : 점수당 등급은 다음과 같습니다.
#        90이상 100이하 : A       
#        80이상 90미만 : B       
#        70이상 80미만 : C      
#        60이상 70미만 : D       
#        60미만 : F

num = int(input("총 과목의 수를 입력하세요: "))

subject=[]

for i in range(1, num+1):
    score = int(input("점수를 입력해주세요: "))
    subject.append(score)

    if score <= 100 and score >= 90:
        print("해당 과목 등급: A")
    elif score <= 90 and score >= 80:
        print("해당 과목 등급: B")
    elif score <= 80 and score >= 70:
        print("해당 과목 등급: C")
    elif score <= 70 and score >= 60:
        print("해당 과목 등급: D")
    else:
        print("해당 과목 등급: F")

subject_sum = sum(subject)

print("총 과목의 평균은 {}입니다.".format(subject_sum / num))