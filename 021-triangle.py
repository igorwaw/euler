#!/usr/bin/python3

from numpy import *

FILENAME='021-triangle-small.txt'
TRSIZE=15

t=zeros((TRSIZE,TRSIZE),dtype=int) # triangle
r=zeros(TRSIZE+1,dtype=int) # routes


def trRead():
	f=open(FILENAME)
	for i in range(TRSIZE):
		s=f.readline()
		numbers=s.split()
		for j in range (len(numbers)):
			t[i][j]=numbers[j]


trRead()
#print t


#for i in range(TRSIZE-10):
i=0
for j in range(i+1):
		road1=t[i,j]+t[i+1,j]+t[i+2,j]
		road2=t[i,j]+t[i+1,j]+t[i+2,j+1]
		road3=t[i,j]+t[i+1,j+1]+t[i+2,j+1]
		road4=t[i,j]+t[i+1,j+1]+t[i+2,j+2]

print("drogi: %d %d %d %d" % (road1,road2,road3,road4))


