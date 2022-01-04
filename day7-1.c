// 반복문을 통해 3의 배수만 *로 출력하기

// 1) for문 이용

#include <stdio.h>

int main()
{
	int n;

	printf("정수를 입력해주세요: ");
	scanf_s("%d", &n);

	for (int i = 1; i <= n; i++)
	{
		if (i % 3 == 0)
		{
			printf("* ");
		}
		else
		{
			printf("%d ", i);
		}
	}

	return 0;
}