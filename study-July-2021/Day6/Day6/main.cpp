// ������ ��� ���ϱ�

// �л��� ���� �Է¹��� ��, �� ����ŭ �л��� ������ �Է¹޾� ����� ���ϴ� ���α׷��� �ۼ��غ�����.

#include <stdio.h>
#include <stdlib.h>

int main()
{
	int num;

	printf("�л��� �� : ");
	scanf_s("%d", &num);

	int* list;
	list = (int*)calloc(num, sizeof(int));

	int average = 0;

	for (int i = 0; i < num; i++)
	{
		printf("�л� %d: ", i + 1);
		scanf_s("%d", &list[i]);
		average += list[i];
	}

	printf("��� : %d", average / num);
	free(list);
}