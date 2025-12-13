#include "maxBinarySum.h"
#include <stdio.h>
#define MAX_NUMBER 1000000000

int binarySum(int number)
{
    int sum = 0;

    while (number > 0) {
        sum += (number & 1);
        number >>= 1;
    }

    return sum;
}

int maxBinarySumNumber(int varA, int varB)
{
    int sumA = binarySum(varA);
    int sumB = binarySum(varB);

    if (sumA > sumB) {
        return varA;
    }
    else if (sumB > sumA) {
        return varB;
    }
    else {
        return 0;
    }
}

int main(void)
{
    int num1;
    int num2;
    int result;

    printf("Введите два положительных целых числа (меньше 1 миллиарда):\n");
    scanf("%d %d", &num1, &num2);

    if (num1 <= 0 || num2 <= 0) {
        printf("Ошибка: числа должны быть положительными\n");
        return 1;
    }

    if (num1 >= MAX_NUMBER || num2 >= MAX_NUMBER) {
        printf("Ошибка: числа должны быть меньше 1 миллиарда\n");
        return 1;
    }

    result = maxBinarySumNumber(num1, num2);

    if (result == 0) {
        printf("Суммы двоичных цифр равны\n");
    }
    else {
        printf("Число с большей суммой двоичных цифр: %d\n", result);
    }

    return 0;
}