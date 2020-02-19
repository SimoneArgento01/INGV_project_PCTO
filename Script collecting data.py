"""
Creazione dei dati JSON
"""
import json
import requests
import re

# convert JSON to Python
x = '{ "Nome":"Simone", "eta":19, "Scuola":"A.VOLTA" }'

# Python creates a new list
y = json.loads(x)

# Python creates a new JSON string
z = json.dumps(y)

print("Tipo:", type(y), y)
print("Tipo:", type(z), z)

# request to HTTP Server
richiesta = requests.get("https://webservices.ingv.it/fdsnws/station/1/query?format=text&net=GU&station=BHB,CIRO&level=station")

# acquiring information about sensors
new = str(richiesta.text)

# preparing values list to insert into memcached
lista = re.split('[|\n]', new)
valori = []

# with the cycle you can delete every characters you don't need (eg. whitespace, backspace, hashtag)
for x in range(len(lista)):

    if lista[x]:
        valori.append(lista[x].strip(' ').strip('#'))

# deleting list1, don't need that
del lista

# create a tuple for having scheme of received data
lista2 = []
for x in range(0, 8):
    lista2.append(valori.pop(0))

# cast of the new created list in a tuple
tupla = tuple(lista2)
del lista2

print(tupla)
print(valori)

# creating an example dictionary (associating -> key:value)
sensori = {}
for x in range(0, 8):
    sensori.update({tupla[x] : valori[x]})

print(sensori)
