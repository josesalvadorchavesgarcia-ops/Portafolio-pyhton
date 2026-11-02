#Listas ----------
listas_frutas=["Perros", "Gatos", "Hamsters" ]
print(listas_frutas)

#Devolver valor

print(listas_frutas[0])
print(listas_frutas[2])

#Modificar valor
listas_frutas[2]= "uva"
print(listas_frutas)

#operaciones con funciones
listas_frutas.append("melon")
print(listas_frutas)
listas_frutas.insert(1,"Sandia")#Insertar en una posicion espesifica
print(listas_frutas)

#Eliminar
listas_frutas.remove("melon")#nombre exacto del elemento
print(listas_frutas)
listas_frutas.pop(1)

#Acomodar de una manera exacta 
listas_frutas.sort()
print(listas_frutas)

#Indica el numero de elementos
print(len(listas_frutas))

#organizar mejor la lista
for fruta in listas_frutas:
    print("esto es una lista de animales:",fruta)
    
#Tuplas
estaciones=("otoño","primavera","verano","invierno")
print(estaciones)
    
    
    
    




