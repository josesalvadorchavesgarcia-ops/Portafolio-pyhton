alumno={"nombre":"Juan",
        "edad"  :"17 años",
        "grupo" :"1A",
        "Especialidad":"Informatica"}
print(alumno)
#llamada
print("El alumno se llama",alumno["nombre"],"y tiene",alumno["edad"],"años")
print("El alumno",alumno.get("nombre"),"tiene este correo:",alumno.get("correo","ninguno"))

#Modificar
alumno["grupo"]="2A"
print(alumno)

#Agregar informacion
alumno["correo"]="juanescl.com"
print(alumno)

#Eliminar
alumno.pop("Especialidad")
print(alumno)
print("++++++++++++++++++++++++++++++++++++++++++++++")
#rECORRIDO
for clave,valor in alumno.items():
    print(clave,":", valor)
    
#Conjuntos
planetas={"Venus","Tierra","Marte","Saturno","Planetas"}
print(planetas)
#Union
grupo_A={"Juan","Maria","Toña"}
grupo_B={"Carlos","Maria","Toña","Salvador"}
print(grupo_A.union(grupo_B))

print("¨************************************")
#Interseccion
grupo_A={"Juan","Maria","Toña"}
grupo_B={"Carlos","Maria","Toña","Salvador"}
print(grupo_A.intersection(grupo_B))
print("*******************************************")
#Difference
grupo_A={"Juan","Maria","Toña"}
grupo_B={"Carlos","Maria","Toña","Salvador"}
print(grupo_A.difference(grupo_B))





































