#!/usr/bin/python3

TARGET=1000

from math import *

numwords={1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4,
	10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8,
	20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6,
	100:7}

def numlen(number):
	if number<21 or (number<100 and number%10==0):
		return numwords[number]
	if (number<100):
		tens=floor(number/10)*10
		ones=number-tens
		#print "tens %d ones %d" % (tens,ones)
		return numlen(tens)+numlen(ones)
	if (number<1000 and number%100==0):
		return 7+numwords[number/100] # 7 liter na "hundred"
	if (number<1000):
		hundreds=floor(number/100)*100
		rest=number-hundreds
		return numlen(hundreds)+numlen(rest)+3 # 3 litery na "and"
	if (number%1000==0):
		return 8+numwords[number/1000] # 8 liter na "thousend"
	
	thousends=floor(number/1000)*1000
	rest=number-thousends
	return numlen(thousends)+numlen(rest)+3 # 3 litery na "and"

#print numlen(10000)

wynik=0
for i in range(1,TARGET+1):
	wynik+=numlen(i)

print(wynik)


