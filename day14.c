//  최솟값 구하기

// 정수 5개를 입력받고, 가장 작은 수를 출력해보세요.

#include <stdio.h>

int main()
{
	int num[5] = { 0. };
	int n = 0, min;

	while (n < sizeof(num) / sizeof(int))
	{
		scanf_s("%d", &num[n]);

		if (n == 0)
		{
			min = num[n];
		}
		else if (min > num[n])
		{
			min = num[n];
		}
		n++;
	}

	printf("\n");
	printf("최소값 : %d", min);

	return 0;
}