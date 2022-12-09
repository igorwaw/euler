#!/usr/bin/python3



TARGET=100

def silnia(liczba):
	wynik=2
	for i in range(3,liczba+1):
		wynik=wynik*i
	return wynik

def sumDigits(liczba):
	napis=str(liczba)
	suma=0
	for i in napis:
		suma+=int(i)
	return suma

print(sumDigits(silnia(TARGET)))

