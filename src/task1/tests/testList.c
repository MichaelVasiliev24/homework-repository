#include "list.h"
#include "testList.h"
#include <stdio.h>
#include <string.h>

// Функция для сравнения списков с массивами
int compareListToArray(List* list, const int* arr, int size)
{
    if (list->size != size) {
        return 0;
    }
    Node* current = list->head;
    for (int i = 0; i < size; i++) {
        if (current == NULL) {
            return 0;
        }
        if (current->data != arr[i]) {
            return 0;
        }
        current = current->next;
    }
    return 1;
}

// Тест инициализации списка
void testInitList(void)
{
    printf("Тест 1: Инициализация списка\n");

    List list;
    initList(&list);

    if (list.head == NULL && list.size == 0) {
        printf("PASS: Список корректно инициализирован\n");
    }
    else {
        printf("FAIL: Ошибка инициализации списка\n");
    }

    printf("\n");
}

// Тест добавления элементов
void testPush(void)
{
    printf("Тест 2: Добавление элементов в список\n");

    List list;
    initList(&list);

    // Тест: Добавление первого элемента
    push(&list, 10);
    int arr1[] = { 10 };
    if (list.size == 1 && list.head->data == 10) {
        printf("PASS: Первый элемент добавлен корректно\n");
    }
    else {
        printf("FAIL: Ошибка добавления первого элемента\n");
    }

    // Тест: Добавление нескольких элементов
    push(&list, 20);
    push(&list, 30);
    int arr2[] = { 10, 20, 30 };
    if (compareListToArray(&list, arr2, 3)) {
        printf("PASS: Несколько элементов добавлены корректно\n");
    }
    else {
        printf("FAIL: Ошибка добавления нескольких элементов\n");
    }

    deleteList(&list);
    printf("\n");
}

// Тест проверки пустоты списка
void testIsEmpty(void)
{
    printf("Тест 3: Проверка пустоты списка\n");

    List list;
    initList(&list);

    // Тест: Пустой список
    if (isEmpty(&list)) {
        printf("PASS: Пустой список распознан корректно\n");
    }
    else {
        printf("FAIL: Пустой список не распознан\n");
    }

    // Тест: Непустой список
    push(&list, 5);
    if (!isEmpty(&list)) {
        printf("PASS: Непустой список распознан корректно\n");
    }
    else {
        printf("FAIL: Непустой список не распознан\n");
    }

    deleteList(&list);
    printf("\n");
}

// Тест проверки симметричности
void testIsSymmetric(void)
{
    printf("Тест 4: Проверка симметричности списка\n");

    // Тест: Пустой список
    List list1;
    initList(&list1);
    if (isSymmetric(&list1)) {
        printf("PASS: Пустой список симметричен\n");
    }
    else {
        printf("FAIL: Пустой список должен быть симметричным\n");
    }
    deleteList(&list1);

    // Тест: Список с одним элементом
    List list2;
    initList(&list2);
    push(&list2, 5);
    if (isSymmetric(&list2)) {
        printf("PASS: Список с одним элементом симметричен\n");
    }
    else {
        printf("FAIL: Список с одним элементом должен быть симметричным\n");
    }
    deleteList(&list2);

    // Тест: Симметричный список (нечетное количество)
    List list3;
    initList(&list3);
    int symOdd[] = { 1, 2, 3, 2, 1 };
    for (int i = 0; i < 5; i++) {
        push(&list3, symOdd[i]);
    }
    if (isSymmetric(&list3)) {
        printf("PASS: Список [1,2,3,2,1] симметричен\n");
    }
    else {
        printf("FAIL: Список [1,2,3,2,1] должен быть симметричным\n");
    }
    deleteList(&list3);

    // Тест: Симметричный список (четное количество)
    List list4;
    initList(&list4);
    int symEven[] = { 1, 2, 2, 1 };
    for (int i = 0; i < 4; i++) {
        push(&list4, symEven[i]);
    }
    if (isSymmetric(&list4)) {
        printf("PASS: Список [1,2,2,1] симметричен\n");
    }
    else {
        printf("FAIL: Список [1,2,2,1] должен быть симметричным\n");
    }
    deleteList(&list4);

    // Тест: Несимметричный список
    List list5;
    initList(&list5);
    int asym[] = { 1, 2, 3, 4, 5 };
    for (int i = 0; i < 5; i++) {
        push(&list5, asym[i]);
    }
    if (!isSymmetric(&list5)) {
        printf("PASS: Список [1,2,3,4,5] не симметричен\n");
    }
    else {
        printf("FAIL: Список [1,2,3,4,5] не должен быть симметричным\n");
    }
    deleteList(&list5);
}

// Запуск всех тестов
void runAllTests(void)
{
    printf("Запуск тестов\n");

    testInitList();
    testPush();
    testIsEmpty();
    testIsSymmetric();

    printf("Все тесты завершены\n");
}