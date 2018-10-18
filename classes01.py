#!/usr/bin/python3
class Dog():
    def __init__(self, nome, raca, iadade):
        self.nome = nome
        self.raca = raca
        self.idade = iadade

    def latir(self):
        print('{} Latindo....'.upper().format(self.nome.upper()))

dog1 = Dog('bilu', 'pitbull', 3)
#dog2 = Dog('rex', 'poddle', 2)



print(dog1.nome, dog1.raca, dog1.idade, sep='\n')
#print(dog2.nome, dog2.raca, dog2.idade, sep='\n')
dog1.latir()
