#Conversion de grados
#Conversion de grados
#Jesus Pedroza Martinez
fahrenheit = int(input('Ingrese una temperatura en grados Fahrenheit: '))
celsius = (fahrenheit - 32) * 5.0/9.0
# Hacemos uso de la funcion str.format() para darle formato a nuestra respuesta
print('{} grados Fahrenheit son {} grados Celsius '.format(fahrenheit, celsius))

print('{} grados Celsius son {} grados Fahrenheit'.format(celsius, fahrenheit))
def fahrenheit_celsius():
    '''convierte temperatura en grados fahrenheit a grados celsius'''
    fahrenheit = int(input('Ingrese la temperatura en grados Fahrenheit: '))
    celsius = (fahrenheit -32 ) * 5.0/9.0
    return '{} grados Fahrenheit son {} grados Celsius'.format(fahrenheit, celsius)
while True:
    print('1.- Fahrenheit a Celsius')

    try:
        opcion = int(input('Seleccione una opción: '))
        if opcion == 1:
            print(fahrenheit_celsius())
    
        elif opcion == 3:
            print('Hasta luego')
        else:
            raise ValueError
    except ValueError:
        print('Ingrese solo números.(1)')
        

        
