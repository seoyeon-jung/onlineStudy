// ���ڿ� ���� �� �� ����ϱ�

/*�� ���� ���ڿ��� �Է� ���� ��, �� ���ڿ� �� �� ���ڿ��� ���̸� ����ϼ���.* *

-�� ���ڿ��� ���̰� ������, �� ���ڿ��� �ϳ��� ���ڿ��� ���ļ� ����ϼ���.
- ���鵵 ���ڿ��� ���̿� �������ּ���.*/

#include <stdio.h>
#include <string.h>

int main()
{
	char x[100];
	char y[100];

	gets_s(x, 100);
	gets_s(y, 100);

	int x_num = strlen(x);
	int y_num = strlen(y);

	if (x_num == y_num)
	{
		strcat_s(x, y);
		printf("%s", x);
	}
	else
		printf("%d", x_num > y_num ? x_num : y_num);
}