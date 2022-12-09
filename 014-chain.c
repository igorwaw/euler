#include <stdio.h>

#define TARGET 1000*1000
#define START TARGET/2+1

inline long long getNext(long long n)
{
	if (n&1)
		return 3*n+1;
	return n/2;
}

/*
inline long long getNext(long long n)
{
	if (n%2==0)
		return n/2;
	else
		return 3*n+1;
}
*/

int main()
{
	int maksimum=1;
	int dla=0;
	long long liczba;
	int dlugosc;
	for (int i=START;i<TARGET+1;i+=2)
	{
		liczba=i;
		dlugosc=1;
		while (liczba>1)
		{
			++dlugosc;
			liczba=getNext(liczba);
		}
		if (dlugosc>maksimum)
		{
			maksimum=dlugosc;
			dla=i;
		}
	}
	printf("maksimum: %d  dla %d",maksimum,dla);

}
