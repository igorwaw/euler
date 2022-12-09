#!/usr/bin/python3

from numpy import *

A=500
B=500


routecache=zeros((A,B),dtype=int)
routecache[0,0]=2

def numRoutes(a,b):
	if routecache[a-1,b-1]>0:
		return routecache[a-1,b-1]
	if (a==1):
		routecache[a-1,b-1]=b+1
		routecache[b-1,a-1]=b+1
		return b+1
	if (b==1):
		routecache[a-1,b-1]=a+1
		routecache[b-1,a-1]=a+1
		return a+1
	tmp=numRoutes(a-1,b)+numRoutes(b-1,a)
	routecache[a-1,b-1]=tmp
	routecache[b-1,a-1]=tmp
	return tmp

print(numRoutes(A,B))

#print routecache

