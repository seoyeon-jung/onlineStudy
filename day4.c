// 관계연산자 사용해보기

#include <stdio.h>

int main()
{
	int x = 10;
	
	printf("오늘은 4일차\n");

	printf("%d\n", ++x != 12);
	printf("%d\n", -x != 9);
	printf("%d\n", x / (x - 5) != 2);
	printf("%d\n", !(x >= 15));

	return 0;
}