#include "../numbersWithoutPair/numbersWithoutPair.h"
#include "testNumbersWithoutPair.h"
#include <stdio.h>
#include <assert.h>

void testHasPair(void)
{
    // Тест: Пара существует
    int test1[] = { 1, 2, 3, 5 };
    assert(hasPair(test1, 4, 1) == 1);
    assert(hasPair(test1, 4, 2) == 1);
    assert(hasPair(test1, 4, 5) == 0);

    // Тест: Пары нет
    int test2[] = { 10, 20, 30 };
    assert(hasPair(test2, 3, 10) == 0);
    assert(hasPair(test2, 3, 20) == 0);
    assert(hasPair(test2, 3, 30) == 0);

    // Тест: Для одинаковых чисел
    int test3[] = { 5, 5, 6 };
    assert(hasPair(test3, 3, 5) == 1);

    // Тест: Для отрицательных чисел
    int test4[] = { -5, -4, 0 };
    assert(hasPair(test4, 3, -5) == 1);
    assert(hasPair(test4, 3, 0) == 0);
}

void testPrintWithoutPair(void)
{
    // Тест: Обычный случай (должно быть 1, 5, 8)
    int test1[] = { 1, 3, 4, 5, 8 };

    // Проверка: какие числа без пары
    int resultCount = 0;
    int expected[] = { 1, 5, 8 };

    for (int i = 0; i < 5; i++) {
        if (!hasPair(test1, 5, test1[i])) {
            assert(test1[i] == expected[resultCount]);
            resultCount++;
        }
    }
    assert(resultCount == 3);

    // Тест: Для каждого числа есть пара
    int test2[] = { 1, 2, 3, 4 };
    for (int i = 0; i < 4; i++) {
        if (i < 3) {
            assert(hasPair(test2, 4, test2[i]) == 1);
        }
    }
}

void testEdgeCases(void)
{
    // Тест: Один элемент
    int test1[] = { 7 };
    assert(hasPair(test1, 1, 7) == 0);

    // Тест: Пустой массив
    int test2[] = {};
    assert(hasPair(test2, 0, 5) == 0);

    // Тест: Числа с большим расстоянием
    int test3[] = { 100, 200 };
    assert(hasPair(test3, 2, 100) == 0);
    assert(hasPair(test3, 2, 200) == 0);
}

int main(void)
{
    printf("Запуск тестов\n\n");

    testHasPair();
    testPrintWithoutPair();
    testEdgeCases();

    printf("Все тесты завершены\n");
    return 0;
}
