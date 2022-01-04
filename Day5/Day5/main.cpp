// 사칙연산 계산기 만들기

//** 함수 포인터를 활용해서 사칙연산 계산기를 만들어 보세요.* *
//
// -두 수를 먼저 입력받습니다.
//- 연산할 기호를 입력받습니다.
//- 해당 기호에 맞는 연산을 실시합니다.

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

	printf("연산 종류 (+, -, *, /) : ");
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