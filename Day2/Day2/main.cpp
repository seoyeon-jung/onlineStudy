//-**��� �� �ٲٱ� * *

// ũ�Ⱑ 4X4�� 2���� �迭�� �Է� �ް�, ��� ���� �ٲ㼭 ����غ�����.


#include <stdio.h>

int main(void)
{
	int arr[4][4] = { 0 };

	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			scanf_s("%d", &arr[i][j]);

	printf("[���� ��] \n");
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
			printf(" %2d", arr[i][j]);
		printf("\n");
	}

	printf("[���� ��] \n");
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
			printf(" %2d", arr[j][i]);
		printf("\n");
	}
}