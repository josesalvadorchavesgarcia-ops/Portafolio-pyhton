#Contraseña correcta 
contraseña_correcta= "abc123"
#Solicitar contraseña
contraseña_ingresada = input("Ingresa la contraseña")

while contraseña_correcta != contraseña_ingresada:
        print("Incorrecta")
        contraseña_ingresada = input("Ingresa la contraseña")

print("Bienvenido")

numero=int(input("ingresa un numero, para crear la tabla de multiplicar"))

for n in range (1,11):
    print(numero * n)