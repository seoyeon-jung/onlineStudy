// ���� ������ ������ ������ ���α׷� �����
// ���� ��ġ�� ���� �߰� �� ���� ������ ������ ����Ǵ� ���α׷��� ��������

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