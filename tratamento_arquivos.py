#!/usr/bin/python3
### w = subescreve
### a = adiciona a ultima linha
### x = se o arquivo ja existe da erro
##### exmplo 1 tipo log
try:
	with open ('file01',x) as f:
		f.write ('\tola\n'):
except FileExistsError as e:
	with open('nome2', 'w') as f:
		f.write ('\tola\n\toi\n\n{}'.format(e))

#### EXEMPLO2
f = open('teste.txt', 'w')
f.white('curso python')
f.close()