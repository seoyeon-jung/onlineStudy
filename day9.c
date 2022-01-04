// - 포인터 연습하기
    
//     두 변수 a와 b를 선언하고, 포인터를 활용해서 
    
//     - 두 변수의 값
//     - 두 변수의 주소값
//     - 두 변수의 값을 바꾼 값
//     - 바꾼 뒤의 주소값
    
//     을 출력해보세요.

#include <stdio.h>

int main() 
{
	int a = 10, b = 15, num;
	int* ptrA = &a, * ptrB = &b;

	printf("a의 값 : %d\na의 주소값 : %p\n\n", *ptrA, ptrA);
	printf("b의 값 : %d\nb의 주소값 : %p\n\n", *ptrB, ptrB);

	num = a;
	a = b;
	b = num;

	printf("바꾼 뒤 a의 값 : %d\n바꾼 뒤 a의 주소값 : %p\n\n", *ptrA, ptrA);
	printf("바꾼 뒤 b의 값 : %d\n바꾼 뒤 b의 주소값 : %p", *ptrB, ptrB);

	return 0;
}