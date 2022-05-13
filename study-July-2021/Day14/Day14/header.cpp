#include "header.h"

void GotoXY(int x, int y) {
	COORD Pos;
	Pos.X = x;
	Pos.Y = y;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), Pos);
}


void CursorViem(char show) {
	CONSOLE_CURSOR_INFO ConsoleCursor;
	ConsoleCursor.bVisible = show;
	ConsoleCursor.dwSize = 1;
	SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &ConsoleCursor);
}

void Move(int* xp, int* yp) {
	int nkey;
	if (_kbhit()) {

		nkey = _getch();

		if (nkey == ARROW) {
			nkey = _getch();

			switch (nkey) {

			case UP:
				(*yp)--;
				GotoXY(*xp, *yp);
				printf("0");
				break;
			case DOWN:
				(*yp)++;
				GotoXY(*xp, *yp);
				printf("0");
				break;
			case LEFT:
				(*xp) -= 2;
				GotoXY(*xp, *yp);
				printf("0");
				break;
			case RIGHT:
				if (*xp + 2 >= 30) {
					exit(0);
				}
				(*xp) += 2;
				GotoXY(*xp, *yp);
				printf("0");
				break;
			}
		}
	}
}
void line() {
	for (int i = 0; i <= 30; i++) {
		GotoXY(30, i);
		printf("¦¢");
	}
}