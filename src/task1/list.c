#include "list.h"
#include <stdio.h>
#include <stdlib.h>

void initList(List* list)
{
    list->head = NULL;
    list->size = 0;
}

int isEmpty(List* list)
{
    return list->head == NULL;
}

Node* createNode(int value)
{
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode == NULL) {
        fprintf(stderr, "Ошибка выделения памяти\n");
        return NULL;
    }
    newNode->data = value;
    newNode->next = NULL;
    return newNode;
}

void push(List* list, int value)
{
    Node* newNode = createNode(value);
    if (newNode == NULL) {
        return;
    }

    if (isEmpty(list)) {
        list->head = newNode;
    }
    else {
        Node* temp = list->head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
    list->size++;
}

int isSymmetric(List* list)
{
    if (isEmpty(list) || list->head->next == NULL) {
        return 1;
    }

    Node* head = list->head;

    Node* slow = head;
    Node* fast = head;

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }

    Node* prev = NULL;
    Node* current = slow;
    Node* next = NULL;

    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    Node* first = head;
    Node* second = prev;

    while (second != NULL) {
        if (first->data != second->data) {
            return 0;
        }
        first = first->next;
        second = second->next;
    }

    return 1;
}

void deleteList(List* list)
{
    Node* current = list->head;
    Node* next;

    while (current != NULL) {
        next = current->next;
        free(current);
        current = next;
    }

    list->head = NULL;
    list->size = 0;
}