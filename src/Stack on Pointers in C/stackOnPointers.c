#include <stdio.h>
#include <stdlib.h>
#include "list.h"

void initializeStack(Stack* ptr) // инициализация стека, выставляем указатель "head" в NULL, а длину - в 0
{
    ptr->head = NULL;
    ptr->len = 0;
}

int isStackEmpty(Stack* ptr) // проверка стека на пустоту; этому состоянию соответствует указатель "head" == NULL
{
    return ptr->head == NULL;
}

void push(Stack* ptr, char value) // положить элемент в стек
{
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode != NULL) {
        newNode->data = value;
        newNode->previuos = ptr->head;
        ptr->head = newNode;
        ptr->len++;
    }
    else {
        printf("Ошибка выделения памяти для нового узла стека\n");
        return;
    }
}

char pop(Stack* ptr) // удалить и при этом посмотреть удаляемый из стека элемент
{
    Node* tempNode = ptr->head;
    char returnData = tempNode->data;
    ptr->head = tempNode->previuos;
    free(tempNode);
    ptr->len--;
    return returnData;
}

char peek(Stack* ptr) // посмотреть элемент в стеке
{
    return ptr->head->data;
}

void deleteStack(Stack* ptr) // удалить стек, осовободить память для всех его узлов (элементов)
{
    while (ptr->head != NULL) {
        Node* tempNode = ptr->head;
        ptr->head = tempNode->previuos;
        free(tempNode);
        ptr->len--;
    }
}