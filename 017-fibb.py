#!/usr/bin/python3

prevfib=1
fib=2
count=3
target=10**999


while (fib<target):
	temp=fib
	fib+=prevfib
	prevfib=temp
	count+=1

print(count)
