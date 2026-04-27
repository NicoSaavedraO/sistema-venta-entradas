import os
os.system("cls")
# El programa debe solicitar:
# •	Nombre del cliente (string) 
# •	Edad del cliente (int) 
# •	Cantidad de entradas (int) 
# •	Precio base de la entrada (float) 
# •	Día de la función: 
# o	"L" = Lunes 
# o	"M" = Martes 
# o	"V" = Viernes 
# o	"S" = Sábado 
# o	"D" = Domingo 
# ________________________________________
# Constantes
# DESCUENTO_NINO = 0.50      # menores de 12 años
# DESCUENTO_ADULTO_MAYOR = 0.30  # 60 años o más
# DESCUENTO_MARTES = 0.20
# RECARGO_FIN_SEMANA = 0.15
# IVA = 0.19
# ________________________________________
#  
# Validaciones (OBLIGATORIAS)
# •	Edad ≥ 0 
# •	Cantidad de entradas > 0 
# •	Precio > 0 
# •	Día válido (L, M, V, S, D) 
# Manejar errores con try-except
# Mostrar mensajes claros sin que el programa falle
DESCUENTO_NINO = 0.50
DESCUENTO_ADULTO_MAYOR = 0.30
DESCUENTO_MARTES = 0.20
RECARGGO_FIN_SEMANA = 0.15
IVA = 0.19

try:
    nombre = str(input("Ingrese su nombre:\n"))
    edad = int(input("Ingrese su edad:\n"))
    while edad < 0:
        edad = int(input("Edad ingresada no válida.\nIngrese la edad nuevamente:\n"))
    cant_entradas = int(input("Ingrese la cantidad de entradas:\n"))
    while cant_entradas < 1:
        cant_entradas = int(input("Cantidad de entradas inválida.\nIngrese la cantidad de entradas nuevamente:\n"))
    precio_entrada = float(input("Ingrese el valor de la entrada:\n"))
    while precio_entrada < 1:
        precio_entrada = float(input("Precio ingresado inválido.\nIngrese el precio de la entrada nuevamente:\n"))
    dia_funcion = int(input("Ingrese el día de la función:\n1. Lunes\n2. Martes\n3. Viernes\n4. Sábado\n5. Domingo\n Miércoles y jueves cerrado.\n"))
    while dia_funcion not in range(1,6):
        dia_funcion = int(input("Día ingresado no válido.\nIngrese el día nuevamente:\n1. Lunes\n2. Martes\n3. Viernes\n4. Sábado\n5. Domingo\n Miércoles y jueves cerrado.\n"))
    subtotal = precio_entrada * cant_entradas
    if edad >= 60:
        desc_edad = subtotal * DESCUENTO_ADULTO_MAYOR
    elif edad < 12:
        desc_edad = subtotal * DESCUENTO_NINO
    else:
        desc_edad = 0
    provi1 = subtotal - desc_edad
    if dia_funcion == 2:
        desc_dia = provi1 * DESCUENTO_MARTES
        provi2 = provi1 - desc_dia
    elif dia_funcion == 4 or dia_funcion == 5:
        desc_dia = provi1 * RECARGGO_FIN_SEMANA
        provi2 = provi1 + desc_dia
    else:
        desc_dia = 0
        provi2 = provi1
    iva = provi2 * IVA
    total_final = provi2 + iva
    total_round = round(total_final,2)
    if total_final <= 10000:
        tipo_compra = "Compra ecónomica."
    elif total_final > 10000 and total_final < 29999:
        tipo_compra = "Compra normal."
    else:
        tipo_compra = "Compra alta."
    print(f"Nombre cliente:\n{nombre}")
    print(f"Edad cliente:\n{edad}")
    if edad < 12:
        print("Tipo de cliente:\nNiño")
    elif edad >= 60:
        print("Tipo de cliente:\nAdulto mayor")
    elif edad in range(12,60):
        print("Tipo de cliente:\nAdulto")
    print(f"Total a pagar:\n{total_round}")
    print(f"Clasificación de compra:\n{tipo_compra}")
except:
    print("Valor ingresado inválido.")
