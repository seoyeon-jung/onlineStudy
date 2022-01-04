// - 팩토리얼 함수 만들기
    
// 정수 N을 입력받고, N 팩토리얼을 구하는 int형 함수를 만들고 값을 출력해보세요.
    
//  **(N팩토리얼) = N x N-1 x N-2 ... x 2 x 1**

#include <stdio.h>

int factorial(int num);

int main() 
{
	int num;

	printf("정수를 입력하세요: ");
	scanf_s("%d", &num);

	int answer = factorial(num);

	printf("\n");
	printf("\n");
	printf("%d 팩토리얼 : %d \n", num, answer);

	return 0;
}

int factorial(int num)
{
	int f = 1;

	for (int i = num; i > 0; i--)
	{
		f *= i;
	}

	return f;
}