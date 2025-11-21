#include <stdio.h>
#include <string.h>
#include "list.h"
#define MAX_INPUT_STRING_SIZE 1000

int openBracket(char value);
int closeBracket(char value);
int matchingBrackets(char valueFirst, char valueSecond);

int main(void)
{
    Stack stack;
    initializeStack(&stack);
    char inputExpression[MAX_INPUT_STRING_SIZE];

    printf("Введите строку: ");
    fgets(inputExpression, sizeof(inputExpression), stdin);
    if (strcspn(inputExpression, "\n") != strlen(inputExpression)) {
        inputExpression[strcspn(inputExpression, "\n")] = '\0';
    }
    unsigned int len = strlen(inputExpression);

    for (unsigned int i = 0; i < len; i++) {
        char currentSymbol = inputExpression[i];
        if (openBracket(currentSymbol)) {
            push(&stack, currentSymbol);
        }
        else if (closeBracket(currentSymbol) && !isStackEmpty(&stack)) {
            if (matchingBrackets(peek(&stack), currentSymbol)) {
                pop(&stack);
            }
            else {
                printf("Баланса нет\n");
                deleteStack(&stack);
                return 1;
            }
        }
        else if (closeBracket(currentSymbol) && isStackEmpty(&stack)) {
            printf("Баланса нет\n");
            return 1;
        }
        else if (!openBracket(currentSymbol) && !closeBracket(currentSymbol)) {
            continue;
        }
    }

    if (isStackEmpty(&stack)) {
        printf("Баланс есть\n");
        return 0;
    }
    else {
        printf("Баланса нет\n");
        deleteStack(&stack);
        return 1;
    }
}

int openBracket(char value)
{
    return (value == '(' || value == '{' || value == '[');
}

int closeBracket(char value)
{
    return (value == ')' || value == '}' || value == ']');
}

int matchingBrackets(char valueFirst, char valueSecond)
{
    switch (valueFirst) {
        case '(':
            return valueSecond == ')';
        case '{':
            return valueSecond == '}';
        case '[':
            return valueSecond == ']';
        default:
            return 0;
    }
}