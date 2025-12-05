all:
	gcc list.c main.c -o program

run:
	./program

test:
	gcc test_list.c list.c -o test_program
	./test_program

clean:
	rm -f program test_program
