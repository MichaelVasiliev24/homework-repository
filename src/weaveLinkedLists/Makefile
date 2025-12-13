all: program test

program: src/linked_list/main.c src/linked_list/linked_list.c src/linked_list/linked_list.h
    gcc src/linked_list/main.c src/linked_list/linked_list.c -o program -Wall -Wextra

test: src/tests/test_linked_list.c src/linked_list/linked_list.c
    gcc src/tests/test_linked_list.c src/linked_list/linked_list.c -o test
    ./test

clean:
    rm -f program test

run: program
    ./program