// 점수의 평균 구하기

// 학생의 수를 입력받은 뒤, 그 수만큼 학생의 점수를 입력받아 평균을 구하는 프로그램을 작성해보세요.

#include <stdio.h>
#include <stdlib.h>

int main()
{
	int num;

	printf("학생의 수 : ");
	scanf_s("%d", &num);

	int* list;
	list = (int*)calloc(num, sizeof(int));

	int average = 0;

	for (int i = 0; i < num; i++)
	{
		printf("학생 %d: ", i + 1);
		scanf_s("%d", &list[i]);
		average += list[i];
	}

	printf("평균 : %d", average / num);
	free(list);
}