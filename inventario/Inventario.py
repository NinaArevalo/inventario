
def Semana_1():


    #Variables 
    #Aqui se hace la solicitud al usuario de agregar el nombre del producto, se utiliza el str para especificar que el dato es en cadena de letras. adicionalmente usamos el input el cual muestra al usuario una pregunta para darle el valor final a la variable nombre.

    nombre = str(input("ingrese el nonmbre del producto: "))

    #Aqui se hace la solicitud al usuario de agregar el precio del producto, usamos el input el cual muestra al usuario una pregunta para darle el valor final a la variable precio.

    precio = (input("Ingrese el precio:"))

    #Se inicia un bucle dando generando una variable y dandole a esta variable un booleano que es True, el blucle usado es While debido a que no sabemos las cantidades finales.
    Validar_precio = True
    while (Validar_precio):

        #dentro del bucle se realizan dos condicionales, en el primero buscamos garantizar que el precio. Adicionalmente se uso, .replace que a modo ejemplo seria: Si tienes un puntito . (porque los precios pueden tener decimales),quítalo solo una vez, para revisar si lo que queda son solo números. y luego el .isdigit para confirmar si lo que queda son solo numeros. Lueo de tener esta informacion le decimos al codigo que ahora me convierta la variable en un numero, es decir que ya no sea texto.
        
        if precio.replace(".", "", 1).isdigit():
            precio=float(precio)
            #dentro de este condicional se agrega uno nuevo el cual nos ayuda a garantizar temas adicionales como de que si el usuario escribe un valor menor o igua a cero debemos indicarle que no es correcto y que ingrese un valor adecuado.
            if precio <= 0:
                print("ingrese un precio valido mayor a 0: ")
            #En este Else ya confirmamos de que el dato es 100% correcto por esta razon dejamos el mensaje “¡Perfecto! El precio es válido, puede continuar.”
            else:
                print("¡Perfecto! El precio es válido, puede continuar.")
                Validar_precio = False
        #finalmente si lo que esta encima no pasa las pruebas entonces el codigo lo pedira nuevamente para poder validar y obtener un valor correcto.
        else:
            print("Error: Valor invalido")
            precio = input("Ingrese el precio")
        
    

    cantidad = (input("ingrese la cantidad: "))
    #dentro del bucle se realizan dos condicionales, en el primero buscamos garantizar que la cantidad sea correcta. Adicionalmente se uso el .isdigit para confirmar si lo que queda son solo numeros. Luego de tener esta informacion le decimos al codigo que ahora me convierta la variable en un numero, es decir que ya no sea texto.
    validar_cantidad = True
    while (validar_cantidad):
        if cantidad.isdigit():
            cantidad = float(cantidad)

            #dentro de este condicional se agrega uno nuevo el cual nos ayuda a garantizar temas adicionales como de que si el usuario escribe un valor menor a cero debemos indicarle que no es correcto y que ingrese un valor adecuado.
            if cantidad < 0:
                print("Cantidad incorrecta, valor debe ser mayor a 0")
            
            #En este Else ya confirmamos de que el dato es 100% correcto por esta razon dejamos el mensaje “Producto guardado”
            else:
                ("Producto guardado")
                validar_cantidad = False
        #finalmente si lo que esta encima no pasa las pruebas entonces el codigo lo pedira nuevamente para poder validar y obtener un valor correcto.
        else:
            print("Error: Cantidad invalida")
            cantidad=input("ingrese cantidad nuevamente: ")


        # aqui finalmente mostramos los datos obtenidos y se los mosntramos al usuario incluyendo la formula de costo total y el porque de ese costo.
        Costo_total = precio * cantidad
        print("Resultado compra")
        print(f"Nombre del producto:   {nombre}")
        print(f"Valor unidad:          {precio}")
        print(f"cantidad de productos: {cantidad}")
        print(f"Costo total:           {Costo_total}")  
def Semana_2():

    def mostrar_Menu():
        #Aqui vamos a mostrarle al usuario un menu al usuario. Agregar producto, Mostrar inventario, calcular estadísticas y Salir. 
        print(""" 
                    Menu
                    
            > 1. Agregar producto
            > 2. Mostrar inventario
            > 3. Calcular estadisticas
            > 4. Salir 
            """)
    def validar_precio():
        #Aqui se hace la solicitud al usuario de agregar el precio del producto, usamos el input el cual muestra al usuario una pregunta para darle el valor final a la variable precio.
        precio = (input("Ingrese el precio:"))

        #Se inicia un bucle dando generando una variable y dandole a esta variable un booleano que es True, el blucle usado es While debido a que no sabemos las cantidades finales.
        Validar_precio = True
        while (Validar_precio):

            #dentro del bucle se realizan dos condicionales, en el primero buscamos garantizar que el precio. Adicionalmente se uso, .replace que a modo ejemplo seria: Si tienes un puntito . (porque los precios pueden tener decimales),quítalo solo una vez, para revisar si lo que queda son solo números. y luego el .isdigit para confirmar si lo que queda son solo numeros. Lueo de tener esta informacion le decimos al codigo que ahora me convierta la variable en un numero, es decir que ya no sea texto.
            
            if precio.replace(".", "", 1).isdigit():
                precio=float(precio)
                #dentro de este condicional se agrega uno nuevo el cual nos ayuda a garantizar temas adicionales como de que si el usuario escribe un valor menor o igua a cero debemos indicarle que no es correcto y que ingrese un valor adecuado.
                if precio <= 0:
                    print("ingrese un precio valido mayor a 0: ")
                #En este Else ya confirmamos de que el dato es 100% correcto por esta razon dejamos el mensaje “¡Perfecto! El precio es válido, puede continuar.”
                else:
                    print("¡Perfecto! El precio es válido, puede continuar.")
                    Validar_precio = False
            #finalmente si lo que esta encima no pasa las pruebas entonces el codigo lo pedira nuevamente para poder validar y obtener un valor correcto.
            else:
                print("Error: Valor invalido")

                precio = input("Ingrese el precio:")

        return precio                    
    def validar_cantidad():
        cantidad = (input("ingrese la cantidad: "))
        #dentro del bucle se realizan dos condicionales, en el primero buscamos garantizar que la cantidad sea correcta. Adicionalmente se uso el .isdigit para confirmar si lo que queda son solo numeros. Luego de tener esta informacion le decimos al codigo que ahora me convierta la variable en un numero, es decir que ya no sea texto.
        validar_cantidad = True
        while (validar_cantidad):
            if cantidad.isdigit():
                cantidad = int(cantidad)

                #dentro de este condicional se agrega uno nuevo el cual nos ayuda a garantizar temas adicionales como de que si el usuario escribe un valor menor a cero debemos indicarle que no es correcto y que ingrese un valor adecuado.
                if cantidad < 0:
                    print("Cantidad incorrecta, valor debe ser mayor a 0")
                
                #En este Else ya confirmamos de que el dato es 100% correcto por esta razon dejamos el mensaje “Producto guardado”
                else:
                    validar_cantidad = False
            #finalmente si lo que esta encima no pasa las pruebas entonces el codigo lo pedira nuevamente para poder validar y obtener un valor correcto.
            else:
                print("Error: Cantidad invalida")
                cantidad=input("ingrese cantidad nuevamente: ")

        return cantidad
    def agregar_product(inventario):

        solicitar_productos=True

        #Aqui se hace la solicitud al usuario de agregar el nombre del producto, adicionalmente usamos el input el cual muestra al usuario una pregunta para darle el valor final a la variable nombre.        
        while(solicitar_productos):
            nombre = (input("ingrese el nombre del producto: "))
            precio = validar_precio()
            cantidad = validar_cantidad()

            #creacion del diccionario
            producto = {
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad,
            }
            #creacion del inventario, aqui con el .append empezamos a agregar la informacion/productos que ingresa el usuario.
            inventario.append(producto)
            print("producto guardado con exito")

            #Preguntar si desea agregar mas productos
            agregar_mas_productos=input("Deseas agregar un nuevo producto: S/N").lower()
            if agregar_mas_productos == "n":
                solicitar_productos = False
            elif agregar_mas_productos == "s":
                continue
            else:
                print("ingrese S o N para confirmar")
        return inventario
    def mostrar_invetario(inventario):
        #aqui usamos len lo cual nos ayuda a garantizar de que si no hay nada en una lista nos lo haga saber, len como tal nos ayuda a saber cuantos productos hay guardados dentro de la lista.
        if len(inventario) == 0:
            print("No hay informacion en el inventario aun.")
            return
        #el siguiente es un bucle for, aqui nos movemos dentro del inventario y traemos informacion especifica, es decir: En la parte de producto de la lista inventario queremos que nos muestre los detalles de ese producto.
        for producto in inventario:
            print(f"Producto: {producto['nombre']} | precio: {producto['precio']} | cantidad:{producto['cantidad']}")       
    def calcular_estadisticas(inventario):
        #aqui llamamos la funcion que necesitamos para encontrar la informacion especifica.
        mostrar_invetario(inventario)
        #usamos len para confirmar si tenemos o no datos en la lista
        if len(inventario) == 0:
            print("no hay productos en el inventario ")
            #este return hace que desde aqui si se cumple el if se devuelva nuevamente a la pregunta inicial.
            return
        #Aqui mencionamos la funcion de valor total la cual podra variar dependiendo de lo que traiga la formula
        Valor_total_inventario = 0
        #El bucle que nos ayuda  arecorrer la lista, busca y trae en la lista inventario en la parte de producto, informacion especifica la cual es el precio y la cantidad, este se multiplica para optener el resultado final.

        for producto in inventario:
            Valor_total_inventario = producto["precio"] * producto["cantidad"]

        print("==========Resultados==========")
        print(f"El valor total del inventario es:", {Valor_total_inventario})
        print("Gracias por tu compra")
        print("==============================")
    def main():
        mostrar_Menu()
        inventario=[]
        continuar=True

        while continuar:
            
            #Aqui hacemos la pregunta al usuario de cual opcion desea escoger
            Menu = input("Que deseas hacer el dia de hoy?, escoge una de las opciones del menu")
            
            #empezamos a garantizar de que el valor ingresado sea un digito con el isdigit(). Ademas, usamos un continue con el fin de que el codigo permita continuar al ser esta una opcion invalida y queremos volver al inicio del bucle para pedir otra vez el dato.
            if not Menu.isdigit(): 
                print("Ingrese una opcion valida")
                continue
            #desde aqui tenemos las diferentes opciones de 1-4 en donde cada una de estas sera valida, se agrega el numero en "" debido a que el usuario lo pondria como texto, pero en cada Elif se usa el int con el fin de cambiar ese dato a numero y ademas, al ser una opcion valida se usa el cierre del bucle.
            elif Menu == "1":
                agregar_product(inventario)        
            elif Menu == "2":
                mostrar_invetario(inventario)           
            elif Menu == "3":
                calcular_estadisticas(inventario)                
            #este else nos garantiza que si ninguna de las opciones de encia son correctas entonces le pedira la informacion nuevamente.
            else:
                print("Saliendo del programa, feliz dia.")            
                continuar=False


        #Nuestro objetivo esta semana ha sido entender como generar una estructuras mas organizada dentro del codigo, generando un menu principal y trabajando desde bloque unilaterales que se combinan al final, adicionalmente, reforzar el uso de dos bucles: while y for, el uso de la logica de forma constante incluyendo en la forma en como hacer operaciones con codigo.
        main()
def Semana_3():
    print ("hi munddo")



   


 