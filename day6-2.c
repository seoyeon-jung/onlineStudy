// 정수 n을 입력받은 후 , n의 값에 따라 음료를 뽑을 수 있는 자판기를 만들어 보세요.

#include <stdio.h>

int main()
{
	int n;

	printf("정수를 입력해주세요 : ");
	scanf_s("%d", &n);

	switch (n)
	{
	case 1:
		printf("콜라가 선택되었습니다.\n");
		break;
	case 2:
		printf("사이다가 선택되었습니다.\n");
		break;
	case 3:
		printf("물이 선택되었습니다.\n");
		break;
	default:
		printf("잘못 입력하셨습니다.\n");
		break;
	}

	return 0;
}