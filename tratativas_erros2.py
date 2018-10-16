#!/usr/bin/python3
a = True 
convidados = ['daniel','maria','joao']
while a == True: 
	try:
		pos = int(input('digite posicao dos convidados:'))
		print (convidados[pos -1])

	except  IndexError as e:
			print ('convidado nao encontrado')

	except  ValueError as e:
			print ('somente numeros')

	except  Exception as e:
			print ('Erro generico')
			
	except  KeyboardInterrupt as e:
			print ('finalizado pelo user')
			a = False	
