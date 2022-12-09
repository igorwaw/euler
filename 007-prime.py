#!/usr/bin/python3

TARGET=10001   #10001

primes=[2,3]
primes_count=2


def nextPrime():
	global primes_count
	a=primes[len(primes)-1]+2
	while (not isPrime(a)):
		a+=1
	primes.append(a)
	primes_count+=1
	return a

def isPrime(b):
	for i in primes:
		if (b%i==0):
			return 0
	return 1


while (primes_count<TARGET):
	nextPrime()

print(primes[-1])
#print primes

