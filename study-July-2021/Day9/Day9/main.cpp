// 사칙연산이 가능한 함수(더하기, 빼기, 곱하기, 나누기) 가 정의되어 있는 "calc.h" 헤더파일을 만들어서 사용해 보세요

#include "calc.h"

int main()
{
	int x, y;
	scanf_s("%d %d", &x, &y);

	cal(x, y);

	return 0;
}