def Saludar():
    nombre = input("Indica tu nombre")
    print("Hola",nombre)
#Comienza el programa formal
def suma(num1,num2):
    resultado = num1 + num2
    print(num1, "+",num2,"=",resultado)

def sumaReturn(num1,num2):
    resultado = num1 + num2
    return resultado



        
        
#Funcion con parametros
def Saludarcon(nombre):
    print("Hola",nombre)

for n in range(1,6):
        Saludar()

Saludarcon("fer")
Saludarcon("Juan")
Saludarcon("Chava")
Saludarcon("Sofia")

suma(5,8)
suma(100,30)

total= sumaReturn(5,8)
print("La suma es igual a",total)
