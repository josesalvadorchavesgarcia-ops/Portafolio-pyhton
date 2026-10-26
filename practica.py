#Solicitar 3 calificaciones
print("promedios")

def promedio(cal1,cal2,cal3):
    resultado=(cal1 + cal2 + cal3)/3
    return resultado

calif1=float(input("Ingresa la 1era calificacion"))
calif2=float(input("Ingresa la 2da calificacion"))
calif3=float(input("Ingresa la 3era calificacion"))

print(promedio(calif1,calif2,calif3))