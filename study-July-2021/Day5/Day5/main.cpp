// ��Ģ���� ���� �����

//** �Լ� �����͸� Ȱ���ؼ� ��Ģ���� ���⸦ ����� ������.* *
//
// -�� ���� ���� �Է¹޽��ϴ�.
//- ������ ��ȣ�� �Է¹޽��ϴ�.
//- �ش� ��ȣ�� �´� ������ �ǽ��մϴ�.

#include <stdio.h>

void plus(int a, int b)
{
	printf("a + b = %d", a + b);
}

void minus(int a, int b)
{
	printf("a - b = %d", a - b);
}

void mul(int a, int b)
{
	printf("a * b = %d", a * b);
}

void div(int a, int b)
{
	printf("a / b = %d", a / b);
}

int main(void)
{
	int x, y;
	int z = 0;
	char n;

	printf("���� ���� (+, -, *, /) : ");
	scanf_s("%c", &n);

	printf("a: ");
	scanf_s("%d", &x);

	printf("b: ");
	scanf_s("%d", &y);

	if (x == '+')
		z = 0;
	else if (x == '-')
		z = 1;
	else if (x == '*')
		z = 2;
	else if (x == '/')
		z = 3;

	void(*ptr[4])(int, int) = { plus, minus, mul,div };
	ptr[z](x, y);

	return 0;
}