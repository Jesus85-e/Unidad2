#Tablas de multiplicar
#Jesus Pedroza
def tablas(numero):
  
    lim = 10
    
    c = 1
    while c <= lim:
        resultado = c * numero
        print("{} x {} = {}".format(numero, c, resultado))
       
        c = c + 1



numero = int(input("Ingrese el numero del cual desea la tabla: \n"))
tablas(numero)

input("")
