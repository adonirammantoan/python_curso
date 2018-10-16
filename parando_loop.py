#!/usr/bin/python3	
cont = 0 

while cont < 10:
	print (cont)
	if cont == 8:
		break
	cont += 1  


impar = []
for num in range (10):
	if num % 2 == 0:
		continue
	impar.append(num)

print(impar)
