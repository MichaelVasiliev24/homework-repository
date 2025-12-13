#include "numbersWithoutPair.h"
#include <stdio.h>
#define MAX_SIZE 1000

int getNumbers(int numbers[])
{
    int count = 0;
    int num;
    printf("Введите целые числа (0 для окончания ввода):\n");
    while (count < MAX_SIZE) {
        scanf("%d", &num);
        if (num == 0) {
            break;
        }
        numbers[count] = num;
        count++;
    }
    if (count == MAX_SIZE) {
        printf("Достигнут максимальный размер (%d чисел)\n", MAX_SIZE);
    }
    return count;
}

int hasPair(const int numbers[], int count, int number)
{
    for (int i = 0; i < count; i++) {
        if (numbers[i] == number + 1) {
            return 1;
        }
    }
    return 0;
}

void printWithoutPair(const int numbers[], int count)
{
    printf("Числа без пары:\n");
    for (int i = 0; i < count; i++) {
        if (!hasPair(numbers, count, numbers[i])) {
            printf("%d ", numbers[i]);
        }
    }
    printf("\n");
}

int main()
{
    int numbers[MAX_SIZE];
    int count;
    count = getNumbers(numbers);
    printWithoutPair(numbers, count);
    return 0;
}