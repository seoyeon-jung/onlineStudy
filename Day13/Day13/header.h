#pragma once

#include <stdio.h>
#include <conio.h>
#include <windows.h>

#define LEFT 75
#define RIGHT 77
#define UP 72
#define DOWN 80
#define ARROW 224

void GotoXY(int x, int y);
void CursorView(char view);
void Move(void);