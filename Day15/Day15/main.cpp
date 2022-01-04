// 미로게임 구현하기
// ***오류들 많아서 수정 필요***

#include "header.h"

void main(void)
{
	int row = 2, col = 1;
	char level;
	CursorView(0);

	GotoXY(XP, YP - 3);
	puts("미로 찾기 게임");
	GotoXY(XP, YP - 2);
	printf("난이도를 선택하세요. (1/2/3) ");
	scanf_s("%c", &level);

	LoadMaze(level);

	start = clock();

	while (1)
	{
		PrintMaze();
		MoveMaze(&row, &col);
	}

}