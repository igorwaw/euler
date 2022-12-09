#!/usr/bin/python3

#2^(15) = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2^(1000)?

TARGET=2**1000

def sumDigits(liczba):
	napis=str(liczba)
	suma=0
	for i in napis:
		suma+=int(i)
	return suma

print(sumDigits(TARGET))


