# Capicua  
numero = input("Ingrese un número entero positivo: ")  

# Verificamos si es un número entero positivo  
if numero.isdigit():  # Compruebamos si la entrada es un número positivo  
    # Aquí vamos comprobar si el número es capicúa  
    if numero == numero[::-1]:  
        print("Es un número capicúa.")  
    else:  
        print("No es un número capicúa.")  
else:  
    print("Entrada no válida. Asegúrate de introducir un número entero positivo.")

    
#Serie de Fibonacci
# Solicitamos al usuario un número entero positivo  
n = input("Ingrese un número entero positivo: ")  

# Verificamos si la entrada es un número entero positivo  
if n.isdigit() and int(n) > 0:  
    n = int(n)  
    
    # Inicializamos lo primeros dos números de Fibonacci  
    fibonacci = [0, 1]  
    
    # Generaramos los números de Fibonacci hasta la variable "n"  
    for i in range(2, n):  
        siguiente = fibonacci[i - 1] + fibonacci[i - 2]  
        fibonacci.append(siguiente)  

    # Limitamos la lista a variable n y convertirla a cadena para mostrar  
    print(", ".join(map(str, fibonacci[:n])))  
else:  
    print("Entrada no válida. ATrate de introducir un número entero positivo.")


#Inverso de un número
# SPedimos al usuario un número entero positivo  
numero = input("Introduce un número entero positivo: ")  

# Verifico si la entrada es un número entero positivo  
if numero.isdigit():  # Compruebando si la entrada es un número positivo  
    # Invertimos el número  
    numero_inverso = numero[::-1]  
    # MostrarAcá aparece el resultado  
    print("Salida:", numero_inverso)  
else:  
    print("Entrada no válida. Trate de introducir un número entero positivo.")


 
#Números Armstrong
# Le solicitamos al usuario un número entero positivo  
numero = input("Introduce un número entero positivo: ")  

# Verifico si la entrada es un número entero positivo  
if numero.isdigit():  
    # Convierto el número en enteros  
    numero = int(numero)  
    
    # Tenemos que convertir el número a una cadena  
    digitos = str(numero)  
    cantidad_digitos = len(digitos)  
    
    # Calculamos la suma 
    suma = sum(int(digito) ** cantidad_digitos for digito in digitos)  

    # Ahora determinamos si el número es Armstrong  
    if suma == numero:  
        print(f"Es un número Armstrong ({' + '.join(f'{int(d)}^{cantidad_digitos}' for d in digitos)} = {numero}).")  
    else:  
        print(f"No es un número Armstrong.")  
else:  
    print("Entrada no es válida. Traatemos de introducir un número entero positivo.")


    #Dígito más grande y más pequeño
      
numero = input("Ingrese un número entero positivo: ")  

# Tengo que verificar si la entrada es un número entero positivo  
if numero.isdigit():  
    # Le convierto cada dígito a entero y almacenarlo en una lista  
    digitos = [int(digito) for digito in numero]  
    
    # Le busco el dígito mayor y menor  
    mayor = max(digitos)  
    menor = min(digitos)  
    
    # MAcá tengo los resultados  
    print(f"Mayor: {mayor}, Menor: {menor}")  
else:  
    print("Entrada no es válida. Tratemos de introducir un número entero positivo.")


#Triángulo de números
 
n = input("Ingresece un número entero positivo: ")  

# Verificar aquí si la entrada es un número entero positivo  
if n.isdigit() and int(n) > 0:  
    n = int(n)  
    
    # Y aca genero un triángulo numérico  
    for i in range(1, n + 1):  
        # Creamos una línea de números del 1 al i  
        fila = ''.join(str(num) for num in range(1, i + 1))  
        print(fila)  
else:  
    print("Entrada no válida. Trate de introducir un número entero positivo.")


#Suma de dígitos de un número hasta ser un solo dígito
 
numero = input("Ingrese un número entero positivo: ")  

# Verifico primero si la entrada es un número entero positivo  
if numero.isdigit() and int(numero) > 0:  
    numero = int(numero)  
    
    while numero >= 10:  # Continua hasta que el número sea de un dígito  
        suma_digitos = sum(int(digito) for digito in str(numero))  
        numero = suma_digitos  # Actualizamos el número con la suma   
    
    # Acá tengo el resultado final  
    print(f"El resultado es {numero}.")  
else:  
    print("Entrada no válida. Asegúrate de introducir un número entero positivo.")


#Suma de números pares e impares
# Solicitar al usuario un número entero positivo  
numero = input("Introduce un número entero positivo: ")  

# Verificar si la entrada es un número entero positivo  
if numero.isdigit() and int(numero) > 0:  
    numero = int(numero)  

    # Inicializar las sumas  
    suma_pares = 0  
    suma_impares = 0  

    # Calcular la suma de pares e impares  
      
numero = input("Ingrese un número entero positivo: ")  

# Verificamos si la entrada es un número entero positivo  
if numero.isdigit() and int(numero) > 0:  
    numero = int(numero)  

    # Comenzamos la suma  
    suma_pares = 0  
    suma_impares = 0  

    # Calculamos la suma de pares e impares  
    for i in range(1, numero + 1):  
        if i % 2 == 0:  
            suma_pares += i  # Sumar si ese número es par  
        else:  
            suma_impares += i  # Sumar si ese número es impar  

    # Acá esta el resultado  
    print(f"Suma de números pares desde 1 hasta {numero}: {suma_pares}")  
    print(f"Suma de números impares desde 1 hasta {numero}: {suma_impares}")  
else:  
    print("Entrada no válida. Asegúrate de introducir un número entero positivo.")


#Cálculo de factorial
 
numero = input("Ingrese un número entero positivo: ")  

# Verificar si es un número entero positivo  
if numero.isdigit() and int(numero) > 0:  
    numero = int(numero)  

    # Hacer los calculos  
    factorial = 1  
    for i in range(1, numero + 1):  
        factorial *= i  # Acá multiplico todos los números enteros positivos desde 1 hasta el número dado  

    # Te muestro el resultado  
    print(f"El factorial de {numero} es: {factorial}")  
else:  
    print("Entrada no válida. Asegúrate de introducir un número entero positivo.")



