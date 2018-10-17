#!/usr/bin/python3
def escopo (nome, idade=18):
	'''Funcao teste'''
	return'nome:{n} idade:{i}'.format(n=nome, i=idade)

a = escopo(nome='teste',idade=10)

print (escopo(nome='teste',idade=55))

print (a)

def teste(*args):
	'''converte em tupla'''
	print(args)

teste('teste', 'teste2')

def teste(**a):
	'''converte em tupla'''
	print(a)

teste('teste:nome1', 'teste2:nome2')