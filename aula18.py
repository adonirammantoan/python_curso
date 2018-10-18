#!/usr/bin/python3
class Dog():
    def __init__(self, nome, raca, idade):
        '''classe dog'''
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.energia = 5


    def latir(self):
        print('{} Latindo....'.upper().format(self.nome.upper()))
    
    def andar(self):
        self.energia -= 1
        print(self.energia)

    def dormir(self):
        self.energia = 5 
    
    def __str__(self):
        return 'Nome: {} Raca: {} Idade: {}'.format(
            self.nome, self.raca, self.idade
        )    

dog1 = Dog('bilu', 'pitbull', 3)
#dog2 = Dog('rex', 'poddle', 2)



print(dog1.nome, dog1.raca, dog1.idade, sep='\n')
#print(dog2.nome, dog2.raca, dog2.idade, sep='\n')
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.dormir()

print(dog1)


print(Dog.__doc__)