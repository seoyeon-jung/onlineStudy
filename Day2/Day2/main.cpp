//-**행과 열 바꾸기 * *

// 크기가 4X4인 2차원 배열을 입력 받고, 행과 열을 바꿔서 출력해보세요.


#include <stdio.h>

int main(void)
{
	int arr[4][4] = { 0 };

	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			scanf_s("%d", &arr[i][j]);

	printf("[변경 전] \n");
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
			printf(" %2d", arr[i][j]);
		printf("\n");
	}

	printf("[변경 후] \n");
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
			printf(" %2d", arr[j][i]);
		printf("\n");
	}
}