#!/usr/bin/python3

prevfib=1
fib=2
sum=count=0

while (fib<4000000):
	temp=fib
	fib+=prevfib
	prevfib=temp
	if fib%2==0:
		print(fib)
		count+=1
		sum+=fib

count+=1
sum+=2

print("count: ",count)
print("sum: ",sum)

