#!/usr/bin/python3
### w = subescreve
### a = adiciona a ultima linha
### x = se o arquivo ja existe da erro
### r = leitura
##### exmplo 1 tipo log
nomes = ['nome1', 'nome2', 'nome3']
for n in nomes: 
	with open ('teste.txt','a') as f:
		f.write ('{}\n'.format(n))