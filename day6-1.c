// 세 수를 입력받고, 그 중 가장 큰 수를 출력해보세요.

#include <stdio.h>

int main()
{
	int x, y, z;

	scanf_s("%d %d %d", &x, &y, &z);

	if (x > y && x > z)
	{
		printf("가장 큰 수는 %d입니다.\n", x);
	}
	else if (y > x && y > z)
	{
		printf("가장 큰 수는 %d입니다.\n" , y);
	}
	else
	{
		printf("가장 큰 수는 %d입니다.\n", z);
	}

	return 0;
}