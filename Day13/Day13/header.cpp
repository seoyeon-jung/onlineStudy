#include "header.h"

void GotoXY(int x, int y)
{
	COORD Pos;
	Pos.X = x;
	Pos.Y = y;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), Pos);
}

void CursorView(char view)
{
	CONSOLE_CURSOR_INFO ConsoleCursor;
	ConsoleCursor.bVisible = view;
	ConsoleCursor.dwSize = 1;
	SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &ConsoleCursor);
}

void Move(void)
{
	int key;
	int x = 25, y = 10;
	GotoXY(x, y);
	CursorView(0);
	printf("0");

	while (1)
	{
		if (_kbhit())
		{
			key = _getch();
			if (key == ARROW)
			{
				key = _getch();
				switch (key)
				{
				case UP:
					if (y != 0)
					{
						system("cls");
						GotoXY(x, y - 1);
						y--;
						printf("0");
						break;
					}
				case DOWN:
					if (y != 80)
					{
						system("cls");
						GotoXY(x, y + 1);
						y++;
						printf("0");
						break;
					}
				case RIGHT:
					if (x != 150)
					{
						system("cls");
						GotoXY(x + 1, y);
						x++;
						printf("0");
						break;
					}
				case LEFT:
					if (x != 0)
					{
						system("cls");
						GotoXY(x - 1, y);
						x--;
						printf("0");
						break;
					}
				}
			}
		}
	}
}