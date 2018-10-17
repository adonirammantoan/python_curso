#!/usr/bin/python3	

quadrado = list(map(lambda x: x **2, range (1,11)))
print (quadrado)
exit()

##### Exemplo de lambada ###
a = lambda x : x ** 2 
quadrado = []
for x in range (1,11):
        quadrado.append(a(x))

b = quadrado 
print (quadrado)
print (b)

### apaga variavel
del a 
del quadrado

#### com list comparate 
quadrado = [(lambda y: y **2)(x) for x in range(1,11,2) if x % 2 != 0]

print (quadrado)