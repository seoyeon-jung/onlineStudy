/*오늘의 문제 : 최대값 구하기**

** 이중 포인터와 크기가 5인 배열을 선언하고, 함수를 사용해서 입력된 수 중 최대값을 출력해보세요.* *

-함수는 void형입니다.
- 최대값을 저장하는 이중 포인터 변수는 main함수에 초기화해야합니다.

 **Hint : 이중 포인터를 사용하면 포인터만 변경된다. */

#include <stdio.h>

void max(int** n);

int main()
{
	int arr[5];
	int* n = arr;

	for (int i = 0; i < 5; i++)
		scanf_s("%d", &arr[i]);

	max(&n);

	return 0;
}

void max(int** numbers)
{
	int max = **numbers;

	for (int i = 1; i < 5; i++)
	{
		if (max < *(*numbers + i))
			max = *(*numbers + i);
	}

	printf("최대값: %d", max);
}