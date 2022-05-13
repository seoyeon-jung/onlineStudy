// 학생 5명 성적 중 최대값 구하기

#include <stdio.h>

int main() 
{
    int num[5] = { 0, };
    int max = 0;

    for (int i = 0; i < sizeof(num) / sizeof(int); i++) 
    {
        printf("학생%d : ", i + 1);
        scanf_s("%d", &num[i]);

        if (max < num[i]) 
        {
            max = num[i];
        }
    }

    printf("최대값 : %d", max);

    return 0;
}