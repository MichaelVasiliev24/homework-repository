#include <stdio.h>
#include <string.h>
#include "list.h"
#define MAX_INPUT_STRING_SIZE 1000

int priority(char symbol);

int main(void)
{
    Stack stack;
    initializeStack(&stack);

    char inputExpression[MAX_INPUT_STRING_SIZE];
    printf("Введите выражение в инфиксной форме: ");
    fgets(inputExpression, sizeof(inputExpression), stdin);
    if (strcspn(inputExpression, "\n") != strlen(inputExpression)) {
        inputExpression[strcspn(inputExpression, "\n")] = '\0';
    }

    unsigned int len = strlen(inputExpression);

    printf("Выражение в постфиксной форме:");

    for (unsigned int i = 0; i < len; i++) {
        char currentSymbol = inputExpression[i];
        if (currentSymbol != '(' && currentSymbol != ')' && currentSymbol != ' ') {
            int currentSymbolPriority = priority(currentSymbol);
            if (currentSymbolPriority == 3) {
                printf(" %c", inputExpression[i]);
            }
            else if (currentSymbolPriority < 3 && !isStackEmpty(&stack)) {
                char operate;
                while (priority(operate = peek(&stack)) <= currentSymbolPriority) {
                    printf(" %c", pop(&stack));
                }
                push(&stack, currentSymbol);
            }
            else if (currentSymbolPriority < 3 && isStackEmpty(&stack)) {
                push(&stack, currentSymbol);
            }
        }
        else if (currentSymbol == '(') {
            push(&stack, currentSymbol);
        }
        else if (currentSymbol == ')') {
            char operateBeforeOpenBracket;
            while ((operateBeforeOpenBracket = pop(&stack)) != '(') {
                printf(" %c", operateBeforeOpenBracket);
            }
        }
        else if (currentSymbol == ' ') {
            continue;
        }
    }

    while (!isStackEmpty(&stack)) {
        printf(" %c", pop(&stack));
    }
    printf("\n");
    return 0;
}

int priority(char symbol)
{
    switch (symbol) {
        case '*':
            return 1;
        case '/':
            return 1;
        case '+':
            return 2;
        case '-':
            return 2;
        default:
            return 3;
    }
}