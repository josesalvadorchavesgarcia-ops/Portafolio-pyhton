#=====================================
#MICROPROYECTO1
#GESTOR DE TAREAS
#DE SALVADOR
#=====================================
print("*********************")
print("Gestor de tareas")#[ ]
print("*********************")

tareas=[]

tarea={
    "nombre":"tarea 1",
    "descripcion":"Terminar proyecto",
    "estado": "pendiente"
    }
tareas.append(tarea)

#Funcion agr tarea
def agregar_tarea():
    nombre=input("Indica el nombre de la tarea:")
    descripcion=input("Descripcion de la tarea:")
    
    tarea={
    "nombre":nombre,
    "descripcion":descripcion,
    "estado": "pendiente"
    }
    tareas.append(tarea)
#Mostrar tarea
def mostrar_tarea():
    for t,tarea in enumerate(tareas):
        print(f"{t+1}.{tarea['nombre']}")
        print(f"Descripcion.{tarea['descripcion']}")
        print(f"Estado.{tarea['estado']}")
        
#Mostrar tareas pendientes
def tareas_pendientes():
    for tarea in tareas:
        if tarea["estado"]=="pendiente":
            print(tarea["nombre"])
            
def completar_tarea():
    mostrar_tarea()
    respuestas=int(input("Numero de tareas a completar"))
    
    tareas[respuestas-1]["estado"]="completado"
    print("Tarea completada")
            
def eliminar_tareas():
    mostrar_tarea()
    respuestas=int(input("Numero de tareas a eliminar"))
    
    tareas[respuestas-1]
    print("Tarea Eliminada")
    
def guardar_tareas():
    with open("tareas.txt","w") as archivo:
        for tarea in tareas:
            archivo.write(tarea["nombre"]+","+tarea["descripcion"]+","+tarea["estado"]+"\n")
respuesta = 0  
while respuesta != 6:
    print("Menu de opciones")
    print("1.Agregar tarea")
    print("2.Mostrar tareas")
    print("3.Mostrar pendientes")
    print("4.Completar tarea")
    print("5.Eliminar tarea")
    print("6.Guardar y salir")
    
    respuesta=int(input(""))
    
    if respuesta ==1:
        agregar_tarea()
    elif respuesta ==2:
        mostrar_tarea()
    elif respuesta ==3:
        tareas_pendientes()
    elif respuesta ==4:
        completar_tarea()
    elif respuesta ==5:
        eliminar_tareas()
    elif respuesta ==6:
        guardar_tareas()
    else:
        print("Opcion no valida")
    

    
