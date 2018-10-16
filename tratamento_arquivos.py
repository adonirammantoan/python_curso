#!/usr/bin/python3
### w = subescreve
### a = adiciona a ultima linha
### x = se o arquivo ja existe da erro
### r = leitura
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

####Leitura de arquivo
with open('file01','r') as f:
	print(f.read())
	b = f.readlines()
	print (b[0] + b[3] + b[6] + '\n' )