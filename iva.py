#iva de una cantidad
#Jesus Pedroza Martinez

def iva():
    '''función básica para el calculo del IVA'''
    iva = 12
    costo = input('¿Cual es el monto a calcular?: ')
    calculo = (costo * iva / 100)
    print ('El calculo de IVA es:' + str(calculo) +'\n')
    
iva()

