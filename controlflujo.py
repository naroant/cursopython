import pprint

lista = []
for i in range(100):
    lista.append(i+1)

pprint.pprint(sorted(lista, reverse=True))