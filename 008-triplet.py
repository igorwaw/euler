#!/usr/bin/python3


# a<b<c
# a^2 + b^2 = c^2
# a + b + c = 1000.
#Find the product abc.

TARGET=1000

def wynik(a,b,c):
	print(a,"^2+",b,"^2 = ",c,"^2")
	print(a*b*c)


for a in range (1,TARGET):
	for b in range (a+1,TARGET):
		c=TARGET-a-b
		if (a**2+b**2==c**2):
			wynik(a,b,c)
			break


