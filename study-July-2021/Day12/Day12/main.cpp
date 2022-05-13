// �� �Ʒ��� �����̴� '��' ����ϱ�
// while���� ���� ����

#include <stdio.h>
#include <windows.h>;

void GotoXY(int x, int y);

void CursorView(char view);

int main(void)
{
	CursorView(0);

	while (1)
	{
		for (int i = 0; i < 25; i++)
		{
			GotoXY(25, i);
			printf("��");
			system("cls");
			Sleep(30);
		}

		for (int j = 24; j > 0; j--)
		{
			GotoXY(25, j);
			printf("��");
			system("cls");
			Sleep(30);
		}
	}
}

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