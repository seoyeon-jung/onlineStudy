 // 학생 정보 입력 받기

 // 사용자로부터 학생의 이름, 나이, 학년, 수학, 영어, 국어 점수를 입력 받고 
 // 이를 평균과 함께 출력하는 프로그램을 작성하세요.

#include <stdio.h>

typedef struct student
{
	char name[20];
	int age;
	int year;
	int math;
	int english;
	int korean;
	int sum;
}Student;

int main()
{
	Student student;

	printf("이름 : ");
	scanf_s("%s", student.name, sizeof(student.name));
	printf("나이 : ");
	scanf_s("%d", &student.age);
	printf("학년 : ");
	scanf_s("%d", &student.year);
	printf("수학 : ");
	scanf_s("%d", &student.math);
	printf("영어 : ");
	scanf_s("%d", &student.english);
	printf("국어 : ");
	scanf_s("%d", &student.korean);

	student.sum = (student.math + student.english + student.korean) / 3;

	printf("\n");
	printf("이름 : %s\n", student.name);
	printf("나이 : %d\n", student.age);
	printf("학년 : %d\n", student.year);
	printf("수학 : %d\n", student.math);
	printf("영어 : %d\n", student.english);
	printf("국어 : %d\n", student.korean);
	printf("평균 점수 : %d\n", student.sum);

	return 0;
}