 // �л� ���� �Է� �ޱ�

 // ����ڷκ��� �л��� �̸�, ����, �г�, ����, ����, ���� ������ �Է� �ް� 
 // �̸� ��հ� �Բ� ����ϴ� ���α׷��� �ۼ��ϼ���.

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

	printf("�̸� : ");
	scanf_s("%s", student.name, sizeof(student.name));
	printf("���� : ");
	scanf_s("%d", &student.age);
	printf("�г� : ");
	scanf_s("%d", &student.year);
	printf("���� : ");
	scanf_s("%d", &student.math);
	printf("���� : ");
	scanf_s("%d", &student.english);
	printf("���� : ");
	scanf_s("%d", &student.korean);

	student.sum = (student.math + student.english + student.korean) / 3;

	printf("\n");
	printf("�̸� : %s\n", student.name);
	printf("���� : %d\n", student.age);
	printf("�г� : %d\n", student.year);
	printf("���� : %d\n", student.math);
	printf("���� : %d\n", student.english);
	printf("���� : %d\n", student.korean);
	printf("��� ���� : %d\n", student.sum);

	return 0;
}