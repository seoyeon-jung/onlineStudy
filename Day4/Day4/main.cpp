// ��� �� ���ϱ�

//3X3 ��� 2���� �����ϰ�, ���� �Է¹��� �� �� ����� ���� ���غ�����.

#include <stdio.h>

void main()
{
	int arrA[3][3];
	int arrB[3][3];
	int result[3][3] = { 0 };

	// ��� A �Է��ϱ�
	printf("[��� A]\n");
	for (int i = 0; i < 3; i++)
		for (int j = 0; j < 3; j++)
			scanf_s("%d", &arrA[i][j]);

	// ��� B �Է��ϱ�
	printf("[��� B]\n");
	for (int i = 0; i < 3; i++)
		for (int j = 0; j < 3; j++)
			scanf_s("%d", &arrB[i][j]);

	// (���) ��� A ����ϱ�
	printf("[��� A]\n");
	for (int i = 0; i < 3; i++)
	{
		for (int j = 0; j < 3; j++)
			printf(" %4d", arrA[i][j]);
		printf("\n");
	}

	// (���) ��� B ����ϱ�
	printf("[��� B]\n");
	for (int i = 0; i < 3; i++)
	{
		for (int j = 0; j < 3; j++)
			printf(" %4d", arrB[i][j]);
		printf("\n");
	}

	// (���) ��� �� ����ϱ�
	printf("[��� ��]\n");
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