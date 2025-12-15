#include <stdio.h>

unsigned int maxCyclicShift(unsigned int num, int bits)
{
    if (bits <= 0 || bits > 32) {
        return num;
    }

    unsigned int maxNum = num;
    unsigned int current = num;

    unsigned int mask = (1U << bits) - 1;

    for (int i = 1; i < bits; i++) {
        unsigned int msb = (current >> (bits - 1)) & 1U;
        current = ((current << 1) | msb) & mask;

        if (current > maxNum) {
            maxNum = current;
        }
    }

    return maxNum;
}

int main(void)
{
    unsigned int num;
    int bits;

    printf("Введите число: ");
    scanf("%u", &num);

    printf("Введите количество бит (N <= 32): ");
    scanf("%d", &bits);

    if (bits <= 0 || bits > 32) {
        printf("Ошибка: количество бит должно быть от 1 до 32\n");
        return 1;
    }

    unsigned int result = maxCyclicShift(num, bits);
    printf("Результат: %u\n", result);

    return 0;
}