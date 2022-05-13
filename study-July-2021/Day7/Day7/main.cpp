// 소수 개수 출력하기

// 임의의 N개의 숫자를 입력받고, 그 중에서 소수인 수의 개수를 출력하는 프로그램을 만들어보세요.

#include <stdio.h>
#include <stdlib.h>

int main()
{
	int numbers = 0;  //숫자 개수 입력

	printf("숫자의 개수 : ");
	scanf_s("%d", &numbers);
	printf("\n");

	int* num;
	num = (int*)malloc(sizeof(int) * numbers);

	int answer = 0;
	int result = 0;

	for (int i = 0; i < numbers; i++)
	{
		scanf_s("%d", &num[i]);

		for (int j = 1; j <= num[i]; j++)
		{
			if (num[i] % j == 0)
			{
				answer++;
			}
		}

		if (answer == 2)
		{
			result++;
			answer = 0;
		}
		else
		{
			answer = 0;
		}
	}

	printf("소수의 개수는 %d입니다.\n", result);

	return 0;
}