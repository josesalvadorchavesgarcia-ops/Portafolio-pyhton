calificacion =int(input("Ingresa la calificacion"))
if calificacion >10:
    print("Fuera de rango")
elif calificacion >=9:
    print("Excelente")
elif calificacion >=7:
    print("bien")
elif calificacion ==6:
    print("aprobo")
elif calificacion <=0:
    print("fuera de rango")
    
    
else:
    print("reprobado")