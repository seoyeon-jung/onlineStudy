// 가장 큰 값 찾기

// 크기가 10인 배열을 입력받은 뒤, 배열 내의 최대값을 구하는 함수를 만들어보세요.

// [조건]

// - 배열 선언 후, 포인터를 활용하세요
// - 함수는 "void"형으로 선언해주세요


#include <stdio.h>

void max(int arrN[]);\

int main()
{
	int arrN[10] = { 0. };
	int* ptrN = arrN;

	for (int i = 0; i < 10; i++)
	{
		scanf_s("%d", &arrN[i]);
	}

	max(ptrN);

	return 0;
}

void max(int arrN[])
{
	int max = arrN[0];
	for (int i = 0; i < 10; i++)
	{
		if (max < arrN[i])
		{
			max = arrN[i];
		}
	}

	printf("\n");
	printf("가장 큰 값: %d\n", max);
}