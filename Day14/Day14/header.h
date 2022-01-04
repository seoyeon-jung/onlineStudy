#ifndef HEADER
#define HEADER
#include <stdio.h>
#include <windows.h>
#include <conio.h>
#define LEFT 75
#define RIGHT 77
#define UP 72
#define DOWN 80
#define ARROW 224


void GotoXY(int x, int y);
void CursorViem(char show);
void Move(int* xp, int* yp);
void line();


#endif