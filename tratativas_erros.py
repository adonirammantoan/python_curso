#!/usr/bin/python3


while True: 
	try:
		x = int (input('digite um numero'))
		y = int (input('digite um numero'))

		print (x + y)

	except  Exception as e:
		print ('apenas numeros')
	
	finally:
		print ('finally')