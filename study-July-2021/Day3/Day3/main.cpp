/*������ ���� : �ִ밪 ���ϱ�**

** ���� �����Ϳ� ũ�Ⱑ 5�� �迭�� �����ϰ�, �Լ��� ����ؼ� �Էµ� �� �� �ִ밪�� ����غ�����.* *

-�Լ��� void���Դϴ�.
- �ִ밪�� �����ϴ� ���� ������ ������ main�Լ��� �ʱ�ȭ�ؾ��մϴ�.

 **Hint : ���� �����͸� ����ϸ� �����͸� ����ȴ�. */

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

	printf("�ִ밪: %d", max);
}