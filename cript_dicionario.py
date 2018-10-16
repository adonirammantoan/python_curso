#!/usr/bin/python3

import sys 
alfabeto = 'abcdefghijklmnopqrstuvwyxz'
chave = 3

def cript(mensagem):
	novo = ''
	for c in mensagem:
		if c in alfabeto:
			indice = alfabeto.index(c)
			novo = novo + alfabeto[(indice + chave)%len(alfabeto)]
		else:
			novo += c
	print (novo)
	
def decript(mensagem):
	novo = ''
	for c in mensagem:
		if c in alfabeto:
			indice = alfabeto.index(c)
			novo = novo + alfabeto[(indice - chave)%len(alfabeto)]
		else:
			novo += c
	print (novo)
def main():
	comando = sys.argv[1].lower()
	mensagem = sys.argv[2].lower()
#	if comando == 'cript':
#		cript(mensagem)
#	elif comando == 'decript':
#		decript(mensagem)
#	else:
#		print ('comando invalido')

	opcoes = {'cript': cript, 'decript': decript}
	opcoes [comando](mensagem)

if __name__=='__main__':
	main()