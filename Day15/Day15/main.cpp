// �̷ΰ��� �����ϱ�
// ***������ ���Ƽ� ���� �ʿ�***

#include "header.h"

void main(void)
{
	int row = 2, col = 1;
	char level;
	CursorView(0);

	GotoXY(XP, YP - 3);
	puts("�̷� ã�� ����");
	GotoXY(XP, YP - 2);
	printf("���̵��� �����ϼ���. (1/2/3) ");
	scanf_s("%c", &level);

	LoadMaze(level);

	start = clock();

	while (1)
	{
		PrintMaze();
		MoveMaze(&row, &col);
	}

}