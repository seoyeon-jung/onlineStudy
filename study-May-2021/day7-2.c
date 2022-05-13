// 반복문을 통해 3의 배수만 *로 출력하기

// 2) while문 이용

#include <stdio.h>

int main()
{
	int n;
	int i = 1;

	printf("정수를 입력해주세요: ");
	scanf_s("%d", &n);

	while (i <= n)
	{
		if (i % 3 == 0)
		{
			printf("* ");
		}
		else
		{
			printf("%d ", i);
		}
		i++;
	}

	return 0;
}