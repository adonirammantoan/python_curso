#!/usr/bin/python3

nomes = ['joao']
s = input ('buscar por nomes')

for nome in nomes:
	if s == nome:
		print ('fora da lista')
		break
else:
	print ('esta na lista')