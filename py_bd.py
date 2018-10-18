#!/usr/bin/python3
import psycopg2
from ex_class import Conta, Poupanca
try:
    con = psycopg2.connect('host=localhost dbname=projeto user=admin password=4linux')
    cur = con.cursor()
except Exception as e:
    print("Erro: {}".format(e))
    exit()
#### Select
#cur.execute("select * from conta;")
#print(cur.fetchall()[0][1])

##### Insert 
#cur.execute("insert into conta(titular, saldo) values ('joao', 7000)")
#con.commit()

cur.execute("select * from conta where id=1;")
pessoa = cur.fetchall()[0][1][:4]
#pessoa = cur.fetchone()
#c1 = Conta(pessoa[1],pessoa[0],pessoa[2])

#print(c1.titular, c1.saldo, c1.numero)
#print(c1)
print(pessoa)



cur.close()
con.close()