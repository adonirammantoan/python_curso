#!/usr/bin/python3
class Conta():
    def __init__(self, titular, numero, saldo=0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def sacar(self, valor):
        if self.saldo < valor:
            return "saldo insuficiente"
        else:
            self.saldo -= valor
            return "saldo realizado com sucesso"

    def depositar(self, valor):
        self.saldo += valor

    def transferir(self, valor, conta):
        try:
            self.saldo -= valor
            conta.depositar(valor) 
            return "Tranferencia realizada"
        except Exception as e:
            return "Erro na transferencia"

    def __str__(self):
        return "nome: {} conta: {} saldo{}".format(
        self.titular, self.numero, self.saldo    
        )   

c1 = Conta('teste',12345,1000)
c2 = Conta('teste2',12346,1000)

c1.transferir(666, c2)
c2.transferir(555, c2)

print (c2.titular, c2.saldo)