#include <math.h>
#include <stdio.h>
#include <stdlib.h>


#define TARGET 600851475143LL

// 600851475143

long long* primes;
int countPrimes;

void addPrime(long long newPrime) 
{ 
	primes[countPrimes]=newPrime; 
	countPrimes++;
}

long long lastPrime()
{
	return primes[countPrimes-1];
}

int isPrime(long long b)
{
	int i;
	for(i=0;i<countPrimes;++i)
	{
		int c=primes[i];
		//printf("c=%d ",c);		
		if(b%c==0)
			return 0;
	}
	return 1;
}

long long nextPrime()
{
	long long a=lastPrime()+2;
	while (! isPrime(a))
		a++;
	addPrime(a);
	return a;	
}

int main()
{
	long long biggestPossible=floor(sqrt(TARGET));
	printf("biggestPossible %lld ",biggestPossible);
	primes=malloc(biggestPossible);
	countPrimes=0;
	addPrime(2); addPrime(3);
	long long i=nextPrime();
	while(i<biggestPossible)
	{
		//printf("%d ",i);
		i=nextPrime();
	}
	printf("primes: %d \n",countPrimes);
	printf("max: %lld \n",lastPrime());
	int gdzie=countPrimes;
	int j=0;
	while(1)
	{
		j=primes[--gdzie];
		//printf("%d ",j);
		if ((TARGET%j==0) && isPrime(TARGET/j))
		{
			printf("wynik %d ",j);
			break;
		}
	}

	free(primes);
	return 0;
}


	/* printf("%d ",biggestPossible);
	if (isPrime(17))
		puts("17 prime");
	if (isPrime(80))
		puts("80 prime");
	else
		puts("80 complex"); */



