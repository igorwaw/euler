#!/usr/bin/python3

from math import sqrt
TARGET= 600851475143
#600851475143

nomore=sqrt(TARGET)
primes=[2,3,5,7,11,13]
factors=[]

def nextPrime():
	a=primes[len(primes)-1]+2
	while (not isPrime(a)):
		a+=1
	primes.append(a)
	return a

def isPrime(b):
	for i in primes:
		if (b%i==0):
			return 0
	return 1

def isInteger(x): return int(x) == x



i=nextPrime()
while (i<nomore):
	i=nextPrime()


print("primes: ")
print(len(primes))
print("max: ")
print(primes[len(primes)-1])
print("wynik: ")
while (1):
	j=primes.pop()
	if (TARGET%j==0 and isPrime(TARGET/j)):
		print(j)
		break
		

#	proba=TARGET/j
#	if (isInteger(proba) and isPrime(proba)):
#		print proba

#	if (TARGET%j==0 and isPrime(TARGET/j)):
#		print TARGET/j

