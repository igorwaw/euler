#!/usr/bin/python3

TARGET=1000000

def getNext(n):
	if (n&1):
		return 3*n+1
	else:
		return n//2

maksimum=1
dla=0
for i in range (TARGET//2+1,TARGET+1,2):
	liczba=i
	dlugosc=1
	while (liczba>1):
		#print liczba,
		dlugosc+=1
		liczba=getNext(liczba)
	if dlugosc>maksimum:
		maksimum=dlugosc
		dla=i
	#print dlugosc

print("maksimum: ",maksimum,"  dla: ",dla)

	
