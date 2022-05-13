// 문자열 길이 비교 후 출력하기

/*두 개의 문자열을 입력 받은 후, 두 문자열 중 긴 문자열의 길이를 출력하세요.* *

-두 문자열의 길이가 같으면, 두 문자열을 하나의 문자열로 합쳐서 출력하세요.
- 공백도 문자열의 길이에 포함해주세요.*/

#include <stdio.h>
#include <string.h>

int main()
{
	char x[100];
	char y[100];

	gets_s(x, 100);
	gets_s(y, 100);

	int x_num = strlen(x);
	int y_num = strlen(y);

	if (x_num == y_num)
	{
		strcat_s(x, y);
		printf("%s", x);
	}
	else
		printf("%d", x_num > y_num ? x_num : y_num);
}