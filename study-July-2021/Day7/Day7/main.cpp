// �Ҽ� ���� ����ϱ�

// ������ N���� ���ڸ� �Է¹ް�, �� �߿��� �Ҽ��� ���� ������ ����ϴ� ���α׷��� ��������.

#include <stdio.h>
#include <stdlib.h>

int main()
{
	int numbers = 0;  //���� ���� �Է�

	printf("������ ���� : ");
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

	printf("�Ҽ��� ������ %d�Դϴ�.\n", result);

	return 0;
}