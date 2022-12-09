#!/usr/bin/python3

from math import *

TARGET=500
BLOCKSIZE=1000


triangles=[]
triangles.append(0)
triangles.append(1)
triangles.append(3)
trcount=2
maxChecked=2
wynik=0

def addNext():
	global trcount
	triangles.append(triangles[trcount]+trcount+1)
	trcount+=1

def addBlock():
	global trcount,BLOCKSIZE
	#print '.',
	for i in range(BLOCKSIZE):
		triangles.append(triangles[trcount]+trcount+1)
		trcount+=1

def countDivisors(liczba):
	if (liczba&1):
		return 0
	uprange=int(floor(sqrt(liczba)))
	ile=2
	for i in range (2,uprange//64):
		if (liczba%i==0):
			ile+=2
	#print liczba,":",ile,"  ",
	return ile


def countDivisorsSimple(liczba):
	ile=2
	for i in range (2,liczba/2):
		if (liczba%i==0):
			ile+=1
	return ile


def printDivisors(liczba):
	print(liczba,": ", end=' ')
	for i in range (1,liczba+1):
		if (liczba%i==0):
			print(i," ", end=' ')
	print()


def checkBlock():
	global trcount,BLOCKSIZE,maxChecked,wynik
	for i in range(maxChecked-1,maxChecked+BLOCKSIZE):
		#print i," ",
		if (countDivisors(triangles[i])>TARGET):
			wynik=i
			return 0
	maxChecked=maxChecked+BLOCKSIZE
	#print
	return 1

notFound=1
while (notFound):
	addBlock()
	notFound=checkBlock()

print()
print(wynik,": ",triangles[wynik])
#printDivisors(triangles[wynik])
#print triangles


