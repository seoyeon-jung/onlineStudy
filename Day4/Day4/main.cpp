// 행렬 곱 구하기

//3X3 행렬 2개를 선언하고, 값을 입력받은 뒤 두 행렬의 곱을 구해보세요.

#include <stdio.h>

void main()
{
	int arrA[3][3];
	int arrB[3][3];
	int result[3][3] = { 0 };

	// 행렬 A 입력하기
	printf("[행렬 A]\n");
	for (int i = 0; i < 3; i++)
		for (int j = 0; j < 3; j++)
			scanf_s("%d", &arrA[i][j]);

	// 행렬 B 입력하기
	printf("[행렬 B]\n");
	for (int i = 0; i < 3; i++)
		for (int j = 0; j < 3; j++)
			scanf_s("%d", &arrB[i][j]);

	// (결과) 행렬 A 출력하기
	printf("[행렬 A]\n");
	for (int i = 0; i < 3; i++)
	{
		for (int j = 0; j < 3; j++)
			printf(" %4d", arrA[i][j]);
		printf("\n");
	}

	// (결과) 행렬 B 출력하기
	printf("[행렬 B]\n");
	for (int i = 0; i < 3; i++)
	{
		for (int j = 0; j < 3; j++)
			printf(" %4d", arrB[i][j]);
		printf("\n");
	}

	// (결과) 행렬 곱 출력하기
	printf("[행렬 곱]\n");
	for (int i = 0; i < 3; i++)
		for (int j = 0; j < 3; j++)
			for (int n = 0; n < 3; n++)
				result[i][j] += arrA[i][n] * arrB[n][j];

	for (int i = 0; i < 3; i++)
	{
		for (int j = 0; j < 3; j++)
			printf(" %4d", result[i][j]);
		printf("\n");
	}
}