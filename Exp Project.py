#Proyecto Final de programación
#Profesora: Nicole Córdoba Coto
#Curso: SC-115
#Integrantes:Gabriel, Juan Carlos Yoilin Mejía
#Año: 2023

#Variables
exit = False
purchases = []
username = ""
buyDay = 0
buyMonth = 0
buyYear = 0
grossTotal = 0
maxItems= 20


#listas
products_quantity = [
    ("Arroz", 2800),
    ("Leche", 1200),
    ("Frijoles", 2000),
    ("Azúcar", 2300),
    ("Garbanzos", 1850),
    ("Lentejas", 1200),
    ("Tomatina", 800),
    ("Caracolitos", 950),
    ("Pasta", 1125),
    ("Atún", 850),  
    ("Sal", 120),  
    ("Maruchan", 500),  
    ("Aceite", 2300),  
    ("Servilletas", 600),  
    ("Lavaplatos", 1350),  
    ("Huevos", 3200),  
    ("Palomitas", 700),  
    ("Champú", 2600),  
    ("Cloro", 1100),  
    ("Desinfectante", 1800),  
    ("Pasta Dental", 1200),  
    ("Alcohol", 900),  
    ("Galletas", 1400),  
    ("Chile Jalapeño", 850),  
    ("Queso Amarillo", 1050),  
]

#funciones
def showProducts():
    print("A continuación, la lista de productos disponibles:\n-------------------------------------------------------")
    for i in range(len(products_quantity)):
        producto, precio = products_quantity[i]
        print(str(i+1) , str(producto) + "-----------" + "precio: ₡" + str(precio))
    
def totalPrice(unitaryPrice, quantity):
    return unitaryPrice * quantity

print("Bienvenido al sistema de facturación supermercado Los Pollitos\n")

while exit == False:
    print ("** MENU *** \n 1) Ingrese nueva compra. \n 2) Salir. ")
    userAns = int(input("Seleccione una opción: "))
    
    if userAns < 0 or userAns >= 3:
        userAns  = int(input("Opción no válida. Digite 1 para volver al menú. "))
    else:
        if userAns == 1:
            print ("Ingresando una nueva compra\n")

            username = input("¿A nombre de quién es la factura? ")
            while username == "":
                print ("Error. Ingrese el nombre nuevamente. ")
                username = input ("¿A nombre de quién es la factura? ")
                
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
            
            
            #Se muestran los productos
            showProducts()
        
            buytarget = "s" 
            while buytarget == "s":
                foodItem = int(input ("Seleccione con números el producto que desea comprar: "))
                
                #validación de productos
                
                #if fooditem <= 1 and fooditem >= len(products_quantity):
                if 1 <= foodItem <= len(products_quantity):
                    itemSelected, unitaryPrice = products_quantity[foodItem - 1]
                    quantity = int(input("Selecionó el producto " + str(itemSelected) + ". ¿Qué cantidad desea llevar? "))
                    
                    # Calcula el monto total del producto
                    priceProduct = totalPrice (unitaryPrice, quantity)
                    
                    #almacena los detalles de la compra en la lista
                    purchases.append((itemSelected, quantity, unitaryPrice, priceProduct))
                
                    # Actualizar el total bruto de la factura
                    grossTotal = grossTotal + priceProduct
                
                    print("Se ha agregado " + str(quantity) + " paquetes de " + str(itemSelected) + " a la compra.")
                
                else:
                    print ("Producto no existente. Intente de nuevo")
                    
                buytarget = str(input ("*******¿Desea ingresar otra compra?******* \nS. continuar.\nN. Salir\nIngrese la opción: " ))
        else:
            if userAns == 2:
                exit = True
print("Ha salido del sistema con éxito. Gracias por su compra.")
            
            
#factura compra
print("\nResumen de la compra:")
print("Cliente:", username)
print("Fecha de compra:", buyDay, "/", buyMonth, "/", buyYear)
print("Productos comprados:")
for purchase in purchases:
    print("Producto:", purchase[0])
    print("Cantidad:", purchase[1])
    print("Precio Unitario: ₡", purchase [2])
    print("Monto total: ₡", purchase[3])
    print("-----------------------")
print("Total bruto de la factura: ₡", grossTotal)