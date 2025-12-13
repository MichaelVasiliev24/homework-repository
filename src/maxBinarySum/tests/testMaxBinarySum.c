#include "testMaxBinarySum.h"
#include "maxBinarySum.h"
#include <stdio.h>
#include <assert.h>

void testBinarySum(void)
{
    assert(binarySum(0) == 0);
    assert(binarySum(1) == 1);
    assert(binarySum(2) == 1);
    assert(binarySum(3) == 2);
    assert(binarySum(4) == 1);
    assert(binarySum(5) == 2);
    assert(binarySum(6) == 2);
    assert(binarySum(7) == 3);
    assert(binarySum(8) == 1);
    assert(binarySum(15) == 4);
    assert(binarySum(255) == 8);
}

void testMaxBinarySumNumber(void)
{
    // Тест: сумма числа A > суммы числа B
    assert(maxBinarySumNumber(7, 4) == 7);

    // Тест: сумма числа B > суммы числа A
    assert(maxBinarySumNumber(1, 3) == 3);

    // Тест: суммы равны
    assert(maxBinarySumNumber(1, 2) == 0);
    assert(maxBinarySumNumber(5, 6) == 0);

    // Тест: обе суммы равны 0
    assert(maxBinarySumNumber(0, 0) == 0);

    // Тест: одинаковые числа
    assert(maxBinarySumNumber(5, 5) == 0);
}

int main(void)
{
    printf("Запуск тестов\n");
    testBinarySum();
    testMaxBinarySumNumber();
    printf("Все тесты завершены\n");
    return 0;
}