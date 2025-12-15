#include "list.h"
#include <stdio.h>

int main()
{
    List list;
    int number;

    initList(&list);

    printf("Введите натуральные числа (0 - конец ввода):\n");

    while (1) {
        scanf("%d", &number);
        if (number <= 0) {
            break;
        }
        push(&list, number);
    }

    if (isSymmetric(&list)) {
        printf("Список симметричен.\n");
    }
    else {
        printf("Список не симметричен.\n");
    }

    deleteList(&list);
    return 0;
}