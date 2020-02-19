def main():
    print("MAYOR y MENOR")
    numero = int(input("ingresa los numeros que deseas compara? "))

    if numero <= 0:
        print("¡Imposible!")
    else:
        valor = float(input("Escriba el nÃºmero 1: "))
        minimo = maximo = suma = valor
        for i in range(2, numero + 1):
            valor = float(input (  " escribe los numeros{i}: "))
            suma = suma + valor
            if valor < minimo:
                minimo = valor
            if valor > maximo:
                maximo = valor
        print(f"El nÃºmero menor de los introducidos es {minimo}")
        print(f"El nÃºmero mayor de los introducidos es {maximo}")
