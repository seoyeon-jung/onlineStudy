// 배열 역순으로 출력하기

#include <stdio.h>

int main() 
{
	int num[5] = { 0, };
	int* ptrN = num;

	for (int i = 0; i < 5; i++)
	{
		scanf_s("%d", &num[i]);
	}

	printf("\n");
	printf("역순으로 출력하기\n");

	for (int j = 4; j >= 0; j--)
	{
		printf("%d\n", *(ptrN + j));
	}

	return 0;
}