#Proyecto Final de programación
#Profesora: Nicole Córdoba Coto
#Curso: SC-115
#Integrantes:Gabriel, Juan Carlos Yoilin Mejía
#Año: 2023

# < menor
# > mayor

#Variables

#userAns = " "

#Saludo

print("Bienvenido al sistema de facturación supermercado Los Pollitos\n")

#Módulo 1. Menú de inicio

userAns  = int(input("Seleccione una opción: \n 1) Ingrese nueva compra. \n 2) Salir. \n Opción: "))

while userAns != 2:

    if userAns == 1:
        print ("Ingresando una nueva compra\n")
        username = str(input("¿A nombre de quién es la factura?"))
        if username == "":
            print ("Error. Ingrese el nombre nuevamente. ")
            username = str(input ("¿A nombre de quién es la factura?"))
            
        buyDay = int(input ("¿Qué día es hoy? "))
        if buyDay > 31:
            print ("Error ingrese la fecha nuevamente. ")
            buyDay = int(input ("¿Qué día es hoy? ")) 
        buyMonth = int(input ("Qué mes está realizando la compra?  "))
        
        if buyMonth > 12:
            print ("Error ingrese el mes nuevamente. ")
            buyMonth = int(input ("¿Qué mes está realizando la compra?"))
        buyYear = int(input ("¿En qué año está realizando la compra?  "))
        
        if buyYear <= 2022:
            print ("Error ingrese el año nuevamente. Tiene que ser mayor al 2022")
            buyYear = int(input ("¿En qué año está realizando la compra? "))
        print("A continuación, la lista de productos son los siguinetes: \n----------------\n")
        
        
    else:
         print ("Ha salido del sistema con éxito. Gracias por su compra")
    userAns  = int(input("Seleccione una opción: \n 1. Ingrese nueva compra. \n 2. Salir \n"))




#Módulo 2. Ingresar nueva compra


print("A continuación, la lista de productos son los siguientes:"
      "\n-------------------------------------------------------\n"
      " 1. Arroz        2. Leche     3. Arroz   4.Arroz     5.Café\n 1. Arroz        2. Leche     3. Arroz   4.Arroz     5.Café\n 1. Arroz        2. Leche     3. Arroz   4.Arroz     5.Café\n"
      
      " 1. Arroz        2. Leche     3. Arroz   4.Arroz     5.Café\n 1. Arroz        2. Leche     3. Arroz   4.Arroz     5.Café\n")
    




