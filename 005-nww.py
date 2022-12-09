#!/usr/bin/python3

TARGET=20
primes=[2,3,5]
primes_count={}
primes_count_temp={}

def nextPrime():
	a=primes[len(primes)-1]+2
	while (not isPrime(a)):
		a+=1
		if (a>=TARGET):
			return a
	primes.append(a)
	return a

def isPrime(b):
	for i in primes:
		if (b%i==0):
			return 0
	return 1

def isInteger(x): return int(x) == x



def zero_count(x):
	for i in primes:
		x[i]=0


i=nextPrime()
while (i<TARGET):
	i=nextPrime()


print("primes: ")
print(len(primes))
print("max: ")
print(primes[len(primes)-1])
zero_count(primes_count)


for i in range(2,TARGET+1):
	liczba=i
	zero_count(primes_count_temp)
	while (liczba>1):	
		for d in primes:
			if (liczba%d==0):
				liczba=liczba/d
				primes_count_temp[d]+=1
				break;
	if (primes_count_temp[d]>primes_count[d]):
		print('.')
		primes_count[d]=primes_count_temp[d];
		#print primes_count_temp
wynik=1

print(primes)
print(primes_count)

print("wynik: ")

for d in primes:
	czynnik=d**primes_count[d]
	print("liczba ",d," ile ", primes_count[d], " czynnik ", czynnik)
	wynik=wynik* czynnik
print(wynik)
