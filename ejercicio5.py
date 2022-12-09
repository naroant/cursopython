esBisiesto = False
def bisiesto(year):
    x = year%4
    y = year%100
    z = year%400

    global esBisiesto

    if x==0 and (y!=0 or (y==0 and z==0)):
        esBisiesto = True

    return esBisiesto

print('Introduce un año')
aConsulta = int(input())

if bisiesto(aConsulta):
    print("El año introducido es bisiesto")
else:
    print("El año introducido no es bisiesto")
