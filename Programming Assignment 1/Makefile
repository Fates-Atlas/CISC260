target: dependencies
	command  # Must be preceded by a TAB, not spaces! 

all: conversion

conversion: main.o binary.o hexadecimal.o
	cc -o conversion main.o binary.o hexadecimal.o $(LDFLAGS)
main.o: main.c conversion.h
	cc -c main.c -I ~/include
binary.o: binary.c conversion.h
	cc -c binary.c -I ~/include
hexadecimal.o: hexadecimal.c conversion.h
	cc -c hexadecimal.c -I ~/include
	
run: all
	./conversion

clean:
	rm -f *.o conversion
