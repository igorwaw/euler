#!/usr/bin/python3

suma=sumakwadratow=0
for i in range (1,101):
    suma+=i
    sumakwadratow+=i*i
print("suma %d" % (suma))
kwadratsumy=suma*suma
print("kwadrat sumy %d" % (kwadratsumy))
print("suma kwadratow %d" % (sumakwadratow))
print("wynik %d" % (kwadratsumy-sumakwadratow))