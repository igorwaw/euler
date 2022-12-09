#!/usr/bin/python3

TARGET=999
t2=TARGET//10
t1=TARGET*t2


palindromy=[]

def isPalindrome(liczba):
	napis=str(liczba)
	odwrocony=napis[::-1]
	if (napis==odwrocony):
		return 1
	else:
		return 0

def check():
	for a in range(TARGET,t2,-1):
		for b in range(TARGET,t2,-1):
			wynik=a*b
			if (wynik==906609):
				print("a=",a," b=",b,"  wynik=",wynik)
			if (wynik<t1):
				break
			if isPalindrome(wynik):
				#print "a=",a," b=",b,"  wynik=",wynik
				palindromy.append(wynik)

check()

palindromy.sort()
print(palindromy[-1])
