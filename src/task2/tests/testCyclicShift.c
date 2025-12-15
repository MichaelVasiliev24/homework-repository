#include "testCyclicShift.h"
#include <stdio.h>

void runTests()
{
    printf("Тестирование циклического сдвига\n");

    int passed = 0;
    int total = 0;

    // Тест: базовый случай
    printf("Тест: Число 5 (101) в 3 битах\n");
    unsigned int result1 = maxCyclicShift(5, 3);
    printf("  Ожидаемый результат: 6 (110)\n");
    printf("  Полученный результат: %u\n", result1);
    if (result1 == 6) {
        printf("PASS\n");
        passed++;
    }
    else {
        printf("FAIL\n");
    }
    total++;
    printf("\n");

    // Тест: Все единицы
    printf("Тест: Число 7 (111) в 3 битах\n");
    unsigned int result3 = maxCyclicShift(7, 3);
    printf("  Ожидаемый результат: 7 (111)\n");
    printf("  Полученный результат: %u\n", result3);
    if (result3 == 7) {
        printf("PASS\n");
        passed++;
    }
    else {
        printf("FAIL\n");
    }
    total++;
    printf("\n");

    // Тест: Один бит
    printf("Тест 4: Число 1 в 1 бите\n");
    unsigned int result4 = maxCyclicShift(1, 1);
    printf("  Ожидаемый результат: 1\n");
    printf("  Полученный результат: %u\n", result4);
    if (result4 == 1) {
        printf("PASS\n");
        passed++;
    }
    else {
        printf("FAIL\n");
    }
    total++;
    printf("\n");

    // Тест: Число 18 (10010) в 5 битах
    printf("Тест: Число 18 (10010) в 5 битах\n");
    unsigned int result5 = maxCyclicShift(18, 5);
    printf("  Ожидаемый результат: 20 (10100)\n");
    printf("  Полученный результат: %u\n", result5);
    if (result5 == 20) {
        printf("PASS\n");
        passed++;
    }
    else {
        printf("FAIL\n");
    }
    total++;
    printf("\n");

    // Тест: Краевой случай - максимальное значение для N бит
    printf("Тест: Число 15 (1111) в 4 битах\n");
    unsigned int result6 = maxCyclicShift(15, 4);
    printf("  Ожидаемый результат: 15 (1111)\n");
    printf("  Полученный результат: %u\n", result6);
    if (result6 == 15) {
        printf("PASS\n");
        passed++;
    }
    else {
        printf("FAIL\n");
    }
    total++;
    printf("\n");

    // Тест: Число 9 (1001) в 4 битах
    printf("Тест: Число 9 (1001) в 4 битах\n");
    unsigned int result7 = maxCyclicShift(9, 4);
    printf("  Ожидаемый результат: 12 (1100)\n");
    printf("  Полученный результат: %u\n", result7);
    if (result7 == 12) {
        printf("PASS\n");
        passed++;
    }
    else {
        printf("FAIL\n");
    }
    total++;
    printf("\n");

    // Итоги
    printf("Итоги\n");
    printf("Пройдено тестов: %d/%d\n", passed, total);
}