// 소수 출력하기

// 정수 N을 입력 받고, N 이하의 소수를 배열에 저장하는 함수를 만들어 보세요.

// - 함수는 "void"형으로 선언해주세요.

#include <stdio.h>

void numbers(int n, int arrN[]);

int main()
{
	int n = 0;
	int arrN[100] = { 0, };

	scanf_s("%d", &n);
	printf("\n소수 출력하기\n");


	for (int i = 2; i <= n; i++)
	{
		arrN[i] = i;
	}

	numbers(n, arrN);

	return 0;
}

void numbers(int n, int arrN[])
{
	for (int i = 2; i <= n; i++)
	{
		if (arrN[i] != 0)
		{
			for (int j = 2 * i; j <= n; j = j+i)
			{
				arrN[j] = 0;
			}
		}
	}

	for (int i = 0; i <= n; i++)
	{
		if (arrN[i] != 0)
		{
			printf("%d ", arrN[i]);
		}
	}
}