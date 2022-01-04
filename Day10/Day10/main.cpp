// 계단 만들기

/*어떠한 양수를 입력받은 뒤, 그 양수와 같은 층의 계단을 만들어보세요**

-GotoXY 함수만을 사용하세요*/

#include <windows.h>
#include <stdio.h>

void GotoXY(int x, int y)
{
	COORD Pos;
	Pos.X = x;
	Pos.Y = y;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), Pos);
}

int main(void)
{
	int a;
	scanf_s("%d", &a);

	for (int i = 0; i < a; i++)
	{
		printf("\n");
		for (int j = 0; j < i; j++)
		{
			printf(" ");
		}
		printf("ㄱ");
	}
}