// 배열 역순으로 저장하고 출력하기

// 크기가 10인 배열을 통해 정수 10개를 입력받고, 이를 역순으로 저장하는 함수를 만들어보세요.

#include <stdio.h>

void numbers(int num[], int size);

void main()
{
	int num[10] = { 0, };
	int* ptrN = num;

	for (int i = 0; i < sizeof(num) / sizeof(int) ; i++)
	{
		scanf_s("%d", &num[i]);
	}

	numbers(ptrN, sizeof(num) / sizeof(int));
}

void numbers(int num[], int size)
{
	int arr_num[10];
	int* pointer = arr_num;
	printf("\n역순으로 출력\n");

	for (int j = 0; j < size; j++)
	{
		*(pointer + j) = num[size - 1 - j];
		printf("%d\n", arr_num[j]);
	}
}