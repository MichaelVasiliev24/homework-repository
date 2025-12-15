#pragma once

typedef struct Node {
    int data;
    struct Node* next;
} Node;

typedef struct List {
    Node* head;
    int size;
} List;

void initList(List* list);
Node* createNode(int value);
void push(List* list, int value);
int isSymmetric(List* list);
void deleteList(List* list);
int isEmpty(List* list);
