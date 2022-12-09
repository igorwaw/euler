#!/usr/bin/python3

TARGET=1000

from math import *

wynik=0
for i in range (1,TARGET+1):
	wynik+=pow(i,i)

print(wynik)


