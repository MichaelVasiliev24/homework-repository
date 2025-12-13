#pragma once

typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* createNode(int data);
Node* createListFromArray(int arr[], int size);
Node* weaveLists(Node* first, Node* second);
void deeleteList(Node* head);
