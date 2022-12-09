import pprint

class Vehiculo:
    color = "negro"
    ruedas = 4
    puertas = 5

class Coche(Vehiculo):
    velocidad = 100
    cilindrada = 125

micoche = Coche()
pprint.pprint(dir(micoche))