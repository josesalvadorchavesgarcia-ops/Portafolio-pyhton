Materias=("Matematicas","Español","Historia","Biologia","inlges")
#Calificaciones
calificaciones=[10,9,8]
#Mostrar las materias y calificaciones
for n in range(0,len(calificaciones)):
    print(Materias[n],":",calificaciones[n])

#Promedio
promedio= sum(calificaciones)/len(calificaciones)
print("promedio:",promedio)
print("++++++++++++++++++++++++++++++")

#Modificar calificacion
calificaciones[2]=10
for n in range(0,len(calificaciones)):
    print(Materias[n],":",calificaciones[n])

print("Existen",len(calificaciones),"Calificaciones registradas")
promedio= sum(calificaciones)/len(calificaciones)
print("promedio:",promedio)
