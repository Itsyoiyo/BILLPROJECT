
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
        
        username = input("¿A nombre de quién es la factura?")
        while username == "":
            print ("Error. Ingrese el nombre nuevamente. ")
            username = input ("¿A nombre de quién es la factura?")
            
        buyDay = int(input ("¿Qué día es hoy? "))
        while buyDay > 31:
            print ("Error ingrese la fecha nuevamente. ")
            buyDay = int(input ("¿Qué día es hoy? ")) 

        buyMonth = int(input ("Qué mes está realizando la compra?  "))
        while buyMonth > 12:
            print ("Error ingrese el mes nuevamente. ")
            buyMonth = int(input ("¿Qué mes está realizando la compra?"))

        buyYear = int(input ("¿En qué año está realizando la compra?  "))
        
        while buyYear <= 2022:
            print ("Error ingrese el año nuevamente. Tiene que ser mayor al 2022")
            buyYear = int(input ("¿En qué año está realizando la compra? "))

        print("A continuación, la lista de productos son los siguientes:\n-------------------------------------------------------\n 1. Arroz        2. Leche     3. Frijoles      4.Azúcar\n")

        buytarget = "s"
        
        while buytarget == "s":
            
            fooditem = int(input (" Seleccione con números el producto que desea comprar: "))
            
            if fooditem == 1:
                food1= "Arroz"
                price1 = 1000
                itemSelected = int(input("Selecció el Arroz, cuesta 1000. ¿Cuántos paquetes desea?"))
                price1item = itemSelected * price1
                print("  ",food1,"              ",itemSelected,"              ",price1item)
            else:
                if fooditem == 2:
                    food2= "Leche"
                    price2 = 1500
                    itemSelected = int(input("Selecció el Leche, cuesta 1500. ¿Cuántos paquetes desea?"))
                    price2item = itemSelected * price2
                    print("  ",food2,"              ",itemSelected,"              ",price2item)
                    
                else:
                    if fooditem == 3:
                        food3= "Frijoles"
                        price3 = 2000
                        itemSelected = int(input("Selecció los Frijoles, cuesta 2000. ¿Cuántos paquetes desea?"))
                        price3item = itemSelected * price3
                        print("  ",food3,"              ",itemSelected,"              ",price3item)
                    else:
                        if fooditem == 4:
                            food4= "Azúcar"
                            price4 = 1700
                            itemSelected = int(input("Selecció el Azúcar, cuesta 1700. ¿Cuántos paquetes desea?"))
                            price4item = itemSelected * price4
                            print("  ",food4,"              ",itemSelected,"              ",price4item)
                        else:
                            print ("Producto no existente. Intente de nuevo")
                            
            buytarget = str(input ("¿Desea ingresar otra compra? s. continuar. n. Salir\n")) #cambiar fooditem por otra variable para reinir el ciclo de compra


        #enseñarle al usuario que ha comprado
        print("--- Datos preliminares de la factura ---- " )
        print("Usuario: ", username)
        print("Fecha de la compra: ", buyDay ,"/", buyMonth, "/", buyYear)
        print(" Producto             Cantidad               Valor")



        
    else:
        print ("Opción no valida. 1. Ingresar nueva compra \n 2. Salir")
    userAns  = int(input("Seleccione una opción: \n 1. Ingrese nueva compra. \n 2. Salir \n"))
print ("Ha salido del sistema con éxito. Gracias por su compra")





