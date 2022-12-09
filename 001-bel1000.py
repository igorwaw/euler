#!/usr/bin/python3

sum = count = 0
for i in range(3, 1000):
	if i%3 ==0:
		sum+=i
		count+=1
		continue
	if i%5 ==0:
		sum+=i
		count+=1
		continue
print(sum)
print(count)


