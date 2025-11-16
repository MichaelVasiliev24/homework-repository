#pragma once
#include <stddef.h>

typedef struct Node {
    char data;
    struct Node* previuos;
} Node;

typedef struct {
    Node* head;
    size_t len;
} Stack;

void initializeStack(Stack* ptr);
int isStackEmpty(Stack* ptr);
void push(Stack* ptr, char value);
char pop(Stack* ptr);
char peek(Stack* ptr);
void deleteStack(Stack* ptr);