#include "testLinkedList.h"
#include "../weavelinkedLists/linkedList.h"
#include <stdio.h>
#include <assert.h>

void testWeaveLists(void)
{
    // Тест: Оба списка одинаковой длины
    int arr1[] = { 1, 3, 5 };
    int arr2[] = { 2, 4, 6 };
    Node* list1 = createListFromArray(arr1, 3);
    Node* list2 = createListFromArray(arr2, 3);

    Node* result = weaveLists(list1, list2);

    Node* current = result;
    assert(current != NULL && current->data == 1);
    current = current->next;
    assert(current != NULL && current->data == 2);
    current = current->next;
    assert(current != NULL && current->data == 3);
    current = current->next;
    assert(current != NULL && current->data == 4);
    current = current->next;
    assert(current != NULL && current->data == 5);
    current = current->next;
    assert(current != NULL && current->data == 6);
    current = current->next;
    assert(current == NULL);

    deleteList(result);

    // Тест: Первый список длиннее
    int arr3[] = { 1, 3, 5, 7 };
    int arr4[] = { 2, 4 };
    Node* list3 = createListFromArray(arr3, 4);
    Node* list4 = createListFromArray(arr4, 2);

    result = weaveLists(list3, list4);

    current = result;
    assert(current != NULL && current->data == 1);
    current = current->next;
    assert(current != NULL && current->data == 2);
    current = current->next;
    assert(current != NULL && current->data == 3);
    current = current->next;
    assert(current != NULL && current->data == 4);
    current = current->next;
    assert(current != NULL && current->data == 5);
    current = current->next;
    assert(current != NULL && current->data == 7);
    current = current->next;
    assert(current == NULL);

    deleteList(result);

    // Тест: Второй список длиннее
    int arr5[] = { 1, 3 };
    int arr6[] = { 2, 4, 6, 8 };
    Node* list5 = createListFromArray(arr5, 2);
    Node* list6 = createListFromArray(arr6, 4);

    result = weaveLists(list5, list6);

    current = result;
    assert(current != NULL && current->data == 1);
    current = current->next;
    assert(current != NULL && current->data == 2);
    current = current->next;
    assert(current != NULL && current->data == 3);
    current = current->next;
    assert(current != NULL && current->data == 4);
    current = current->next;
    assert(current != NULL && current->data == 6);
    current = current->next;
    assert(current != NULL && current->data == 8);
    current = current->next;
    assert(current == NULL);

    deleteList(result);

    // Тест: Первый список пустой
    Node* list7 = NULL;
    int arr8[] = { 1, 2, 3 };
    Node* list8 = createListFromArray(arr8, 3);

    result = weaveLists(list7, list8);
    assert(result == list8);

    deleteList(result);

    // Тест: Второй список пустой
    int arr9[] = { 1, 2, 3 };
    Node* list9 = createListFromArray(arr9, 3);
    Node* list10 = NULL;

    result = weaveLists(list9, list10);
    assert(result == list9);

    deleteList(result);
}

int main(void)
{
    printf("Запуск тестов\n");
    testWeaveLists();
    printf("Все тесты завершены\n");
    return 0;
}