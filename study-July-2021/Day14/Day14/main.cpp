// 선에 닿으면 게임이 끝나는 프로그램 만들기
// 일정 위치에 선을 긋고 그 선에 닿으면 게임이 종료되는 프로그램을 만들어보세요

#include "header.h"

int main(void) {
	CursorViem(0);
	int x = 15, y = 15;
	GotoXY(x, y);

	while (1) {
		system("cls");
		Move(&x, &y);
		line();
		Sleep(100);
	}
	return 0;
}