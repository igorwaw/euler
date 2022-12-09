#!/usr/bin/python3

TARGET=2000000
pprimes=[]

def isPrime(b):
	return pprimes[b]

def removeMultiples(liczba,limit):
	global pprimes
	#print "usuwam wielokrotnosc ",liczba
	for i in range (liczba*2,limit,liczba):
		pprimes[i]=0		
		

def sieve(limit):
	global pprimes
	for i in range(limit):
		pprimes.append(1)
	pprimes[0]=pprimes[1]=0
	for i in range(2,limit):
		if isPrime(i):
			removeMultiples(i,limit)

def pokaz():
	i=0
	for a in pprimes:
		if a==1:
			print(i)
		i+=1

def sumuj():
	suma=i=0
	for a in pprimes:
		if a==1:
			suma+=i
		i+=1
	return suma

sieve(TARGET+1)
print(sumuj())

#pokaz()

