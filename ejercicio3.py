
print("¿Cuánto pesa (en kg)?")
peso = float(input())
print("¿Cuánto mide (en m)?")
altura = float(input())

IMC = peso/(altura**2)

print("Su índice de masa corporal es de ",round(IMC,2),".")

