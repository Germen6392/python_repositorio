print("Factura de electricidad") # Titulo


def menu():
    print("opcion 1: tarifa residencial")
    print("opcion 2: tarifa comercial")
    print("opcion 3: salir")

    
menu()


# es valido en tarifa comercial o residencial

opcion = int(input("ingrese una opcion del menu (en numero): "))

def salir():
    if opcion == 3:
        print("usted decidio salir. gracias por utilizar el programa")

def ahorro(opcion):
    if opcion == 1:
        if consumo <= 400:
            bonif = 250 # bonif = bonificacion
            tot_mens = round(monto_mens - bonif,2)  # tot_mens = total mensual

            print(f"su factura es de {consumo}kw, tiene ahorro y debe abonar ${tot_mens}")
        else:
            print(f"su factura es de {consumo}kw, esta excedido y debe abonar ${monto_mens}")
    else:
        if consumo <= 500:
            bonif = 180
            tot_mens = round(monto_mens - bonif,2)
            print(f"su factura es de {consumo}kw, tiene ahorro y debe abonar ${tot_mens}")
        else:
            print(f"su factura es de {consumo}kw, esta excedido y debe abonar ${monto_mens}")
   
# datos
precio_kw = [4.47,7.54]
cargo_fijo=[61.44,85.22]
impuesto=1.21
alum_pb=[950,1010]
ing_bruto=0.25
iva=1.21

# opciones del programa
if opcion == 1:
    print("tarifa residencial")
    
    lectura_anterior =int(input("ingrese lectura periodo anterior: "))
    lectura_actual =int(input("ingrese lectura periodo actual: "))
    consumo = lectura_actual - lectura_anterior
    monto = precio_kw[0] * consumo + cargo_fijo[0] + impuesto + alum_pb[0]
    monto_mens = monto / 2 #monto_mens = monto mensual 
#el periodo que se toma entre lecturas es bimestral pero despues se facturara mensual
    tot_mens = ahorro(1)
   
elif opcion == 2:
   print("tarifa comercial")
    
   lectura_anterior =int(input("ingrese lectura periodo anterior: "))
   lectura_actual =int(input("ingrese lectura periodo actual: "))
   consumo = lectura_actual - lectura_anterior
   monto = precio_kw[1] * consumo + cargo_fijo[1] + alum_pb[1] + iva + ing_bruto
   monto_mens = monto / 2
   tot_mens = ahorro(2)
else:
   salir() 
