numeros = []
valor = ""
menor = ""
mayor = ""

for x in range(4):
    valor=int(input("Ingrese un valor entero: "))
    numeros.append(valor)

for numero in numeros:
    valor = valor + str(numero)

numeros.sort()
for num in numeros:
    menor = menor + str(num)

numeros.reverse()
for x in numeros:
    mayor = mayor + str(x)

print(f"Numero ingresado: {valor}")
print(f"Mayor num posible: {mayor}")
print(f"Menor num posible: {menor}")
print(f"Resta entre ambos: {int(mayor)-int(menor)}")