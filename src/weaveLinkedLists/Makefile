all: program test

program: src/weaveLinkedLists/linkedList.c src/weaveLinkedLists/linkedList.h
	gcc src/weaveLinkedLists/linkedList.c -o program -Wall -Wextra

test: src/tests/testLinkedList.c src/weaveLinkedLists/linkedList.c
	gcc src/tests/testLinkedList.c src/weaveLinkedLists/linkedList.c -o test
	./test

clean:
	rm -f program test

run: program
	./program
