// ��� �����

/*��� ����� �Է¹��� ��, �� ����� ���� ���� ����� ��������**

-GotoXY �Լ����� ����ϼ���*/

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
		printf("��");
	}
}