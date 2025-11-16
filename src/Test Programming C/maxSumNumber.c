#include <stdio.h>
#include <stdlib.h>

int maxSumNumber(int* ptr, int len);
int sumNumber(int num);

int main(void)
{

    int lenArr;
    printf("Введите размер массива: ");
    scanf("%d", &lenArr);

    int* inputArr = (int*)malloc(lenArr * sizeof(int));

    for (int i = 0; i <= lenArr - 1; i++) {
        printf("Введите %d  число массива: \n", i + 1);
        scanf("%d", &inputArr[i]);
    }

    int maxSumNumberInArr = maxSumNumber(inputArr, lenArr);

    for (int i = 0; i <= lenArr - 1; i++) {
        if (sumNumber(inputArr[i]) == maxSumNumberInArr) {
            printf("Число из массива с максимальной суммой цифр: %d\n", inputArr[i]);
        }
    }
    free(inputArr);
    return 0;
}

int sumNumber(int num)
{
    int ost;
    int sum = 0;
    num = abs(num);
    if (num < 10) {
        return num;
    }
    else {
        while ((ost = num % 10) != 0) {
            sum += ost;
            num /= 10;
        }
        return sum;
    }
}

int maxSumNumber(int* ptr, int len)
{
    int maxSum = 0;
    for (int i = 0; i <= len - 1; i++) {
        if (maxSum <= sumNumber(ptr[i])) {
            maxSum = sumNumber(ptr[i]);
        }
        else {
            continue;
        }
    }
    return maxSum;
}