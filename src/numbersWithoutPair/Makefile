all: program test_program

program: src/numbersWithoutPair/numbersWithoutPair.c
    gcc src/numbersWithoutPair/numbersWithoutPair.c -o program -Wall -Wextra

test_program: src/tests/testNumbersWithoutPair.c src/numbersWithoutPair/numbersWithoutPair.c
    gcc src/tests/testNumbersWithoutPair.c src/numbersWithoutPair/numbersWithoutPair.c -o test_program
    ./test_program

clean:
    rm -f program test_program

run: program
    ./program

test: test_program