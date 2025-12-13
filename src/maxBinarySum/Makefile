all: program test

program: src/maxBinarySum/maxBinarySum.c src/maxBinarySum/maxBinarySum.h
    gcc src/maxBinarySum/maxBinarySum.c -o program -Wall -Wextra

test: src/tests/testMaxBinarySum.c src/maxBinarySum/maxBinarySum.c
    gcc src/tests/testMaxBinarySum.c src/maxBinarySum/maxBinarySum.c -o test
    ./test

clean:
    rm -f program test

run: program
    ./program