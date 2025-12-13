#include "linkedList.h"
#include <stdio.h>
#include <stdlib.h>

Node* createNode(int data)
{
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode == NULL) {
        printf("Ошибка выделения памяти\n");
        return NULL;
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

Node* createListFromArray(int arr[], int size)
{
    if (size == 0) {
        return NULL;
    }

    Node* head = createNode(arr[0]);
    Node* current = head;

    for (int i = 1; i < size; i++) {
        current->next = createNode(arr[i]);
        current = current->next;
    }

    return head;
}

void deleteList(Node* head)
{
    Node* current = head;
    while (current != NULL) {
        Node* next = current->next;
        free(current);
        current = next;
    }
}

Node* weaveLists(Node* first, Node* second)
{
    if (first == NULL) {
        return second;
    }
    if (second == NULL) {
        return first;
    }

    Node* result = first;
    Node* currentFirst = first;
    Node* currentSecond = second;
    Node* tempFirst;
    Node* tempSecond;

    while (currentFirst != NULL && currentSecond != NULL) {
        tempFirst = currentFirst->next;
        tempSecond = currentSecond->next;

        currentFirst->next = currentSecond;

        if (tempFirst != NULL) {
            currentSecond->next = tempFirst;
        }
        currentFirst = tempFirst;
        currentSecond = tempSecond;
    }

    return result;
}
